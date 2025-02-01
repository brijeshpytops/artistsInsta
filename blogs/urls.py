from django.urls import path
from .views import *

urlpatterns = [
    path('', login, name='login'),
    path('register/', register, name='register'),
    path('forgot-password/', forgot_password, name='forgot_password'),
    path('otp-verify/', otp_verify, name='otp_verify'),
    path('logout/', logout, name='logout'),
    path('home/', home_view, name='home_view'),
    path('photography/', photography_view, name='photography_view'),
    path('blogs/', blogs_view, name='blogs_view'),
    path('about/', about_view, name='about_view'),
    path('contact/', contact_view, name='contact_view'),
]
    