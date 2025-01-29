from django.shortcuts import render

# Create your views here.
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