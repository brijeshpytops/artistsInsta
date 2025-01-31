from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'blogs/login.html')

def register(request):
    return render(request, 'blogs/register.html')

def forgot_password(request):
    return render(request, 'blogs/forgot-password.html')

def otp_verify(request):
    return render(request, 'blogs/otp-verify.html')

def home_view(request):
    return render(request, 'blogs/home.html')

def photography_view(request):
    return render(request, 'blogs/photography.html')

def blogs_view(request):
    return render(request, 'blogs/blogs.html')

def about_view(request):
    return render(request, 'blogs/about.html')

def contact_view(request):
    return render(request, 'blogs/contact.html')