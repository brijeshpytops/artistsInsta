from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import send_mail
from django.conf import settings

from functools import wraps

from .models import Artist, Post, Photography, Contacts

import random

# Create your views here.
def artist_login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if 'artist_id' in request.session:
            return view_func(request, *args, **kwargs)
        else:
            messages.warning(
                request,
                "You must be logged in to access this page. Please login or register."
            )
            return redirect('login')  # Redirect to login if not authenticated
    return wrapper


def validate_password(request, password_):
    # List of validation checks with corresponding error messages
    validations = [
        (len(password_) >= 8, "Password should be at least 8 characters long."),
        (any(char.isupper() for char in password_), "Password should contain at least one uppercase letter."),
        (any(char.islower() for char in password_), "Password should contain at least one lowercase letter."),
        (any(char.isdigit() for char in password_), "Password should contain at least one digit."),
        (any(char in "!@#$%^&*()-_+=<>?/{}[]|\\:;." for char in password_), "Password should contain at least one special character."),
    ]

    # Check each condition
    for condition, message_text in validations:
        if not condition:
            messages.warning(request, message_text)
            return redirect('register')

    # If all validations pass
    return None

def login(request):
    if request.method == 'POST':
        email_ = request.POST['email']
        password_ = request.POST['password']

        get_artist = Artist.objects.filter(email=email_).exists()
        if get_artist:
            artist = Artist.objects.get(email=email_)
            if check_password(password_, artist.password):
                request.session['artist_id'] = str(artist.art_id)
                request.session['first_name'] = artist.first_name
                request.session['last_name'] = artist.last_name
                return redirect('home_view')
            else:
                messages.info(request, "Incorrect email or password.")
                return redirect('login')
        else:
            messages.info(request, "Incorrect email or password.")
    return render(request, 'blogs/login.html')

def register(request):
    if request.method == 'POST':
        first_name_ = request.POST['first_name']
        last_name_ = request.POST['last_name']
        email_ = request.POST['email']
        mobile_ = request.POST['mobile']
        password_ = request.POST['password']
        confirm_password_ = request.POST['confirm_password']

        # Validation
        # Check if email already exists
        if Artist.objects.filter(email=email_).exists():
            messages.info(request, f'"{email_}" already exists. Please try with a different one.')
            return redirect('register')
        
        # Check if mobile number already exists
        if Artist.objects.filter(mobile=mobile_).exists():
            messages.info(request, f'"{mobile_}" already exists. Please try with a different one.')
            return redirect('register')
        
        # Check password
        validation_error = validate_password(request, password_)
        if validation_error:
            return validation_error
        
        # Check if password and confirm password match
        if password_!=confirm_password_:
            messages.info(request, "Password and Confirm Password do not match.")
            return redirect('register')
        
        # Insert Queryset - use create method
        new_artist = Artist.objects.create(
            first_name=first_name_,
            last_name=last_name_,
            email=email_,
            mobile=mobile_,
            password=make_password(password_),
            is_active=True
        )
        messages.success(request, f'Registration Successful. You can now Login.')
        new_artist.save()   
        return redirect('login')     

    return render(request, 'blogs/register.html')

def forgot_password(request):
    if request.method == 'POST':
        email_ = request.POST['email']
        get_artist = Artist.objects.filter(email=email_).exists()
        if get_artist:
            artist = Artist.objects.get(email=email_)
            otp_ = random.randint(1111, 9999)
            subject = 'Reset Password OTP Code | ArtistBlogs'
            message = f"""
            Hello {artist.first_name} {artist.last_name}

            We have received a request to reset your password. Please use the OTP code below to complete the process.

            OTP Code: {otp_}

            If you did not request this password reset, please ignore this message.

            Regards,
            ArtistBlogs Team
            """
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [f'{email_}']
            send_mail(subject, message, from_email, recipient_list)
            artist.otp =  otp_
            artist.save()
            messages.success(request, f'An OTP has been sent to your registered mobile number.')
            return render(
                request,
                'blogs/otp-verify.html',
                {'email':email_}
            )
        else:
            messages.info(request, f'"{email_}" is not registered. Please try with a different one.')
            return redirect('forgot_password')
    return render(request, 'blogs/forgot-password.html')

def otp_verify(request):
    if request.method == 'POST':
        otp_ = request.POST['otp']
        email_ = request.POST['email']
        new_password_ = request.POST['new_password']
        confirm_password_ = request.POST['confirm_password']
        artist = Artist.objects.get(email=email_)
        
        if artist.otp == otp_:
            if new_password_!= confirm_password_:
                messages.info(request, 'Password and Confirm Password do not match.')
                return render(
                    request,
                    'blogs/otp-verify.html',
                    {'email':email_}
                )
            else:
                artist.password = make_password(new_password_)
                artist.save()
                messages.success(request, 'Password has been changed successfully.')
                return redirect('login')
        else:
            messages.info(request, 'Incorrect OTP. Please try again.')
            return render(
                request,
                'blogs/otp-verify.html',
                {'email':email_}
            )
    return render(request, 'blogs/otp-verify.html')

def logout(request):
    if request.session.get('artist_id'):
        del request.session['artist_id']
        del request.session['first_name']
        del request.session['last_name']
    
    messages.success(request, 'Now, you are logged out.')
    return redirect('login')

@artist_login_required
def home_view(request):
    return render(request, 'blogs/home.html')

@artist_login_required
def photography_view(request):
    artist_id = request.session['artist_id']
    if request.method == 'POST':
        img_ = request.FILES.get('image')
        tag_ = request.POST['tag']

        new_work = Photography.objects.create(
            artist_id=artist_id,
            photo_img=img_,
            photo_tag=tag_
        )
        new_work.save()
        messages.success(request, 'Work has been uploaded successfully.')
        return redirect('photography_view')

    get_works = Photography.objects.filter(artist_id=artist_id).order_by('-created_at')
    context = {'works': get_works}
    return render(request, 'blogs/photography.html', context)

@artist_login_required
def posts_view(request):
    if request.method == 'POST':
        artist_id = request.session['artist_id']
        img_ = request.FILES.get('post_img')
        tag_ = request.POST['post_tag']
        title_ = request.POST['post_title']
        content_ =request.POST['content']

        new_post = Post.objects.create(
            artist_id=artist_id,
            post_img=img_,
            post_tag=tag_,
            post_title=title_,
            content=content_
        )
        new_post.save()
        messages.success(request, 'Post has been created successfully.')
        return redirect('posts_view')
    
    get_posts = Post.objects.all().order_by('-created_at')
    context = {'posts': get_posts[:10]}
    return render(request, 'blogs/posts.html', context)

@artist_login_required
def about_view(request):
    return render(request, 'blogs/about.html')

@artist_login_required
def contact_view(request):
    return render(request, 'blogs/contact.html')