# artistsBolgs
artistsBolgs

- Create Repo in github setup in local PC and open CMD
(sepcific-location)>>> git clone https://github.com/brijeshpytops/[repoName].git

(sepcific-location)>>>cd [repoName]
([repoName])>>>

- Make sure you have installed python in your local PC
([repoName])>>> python --version
Python 3.12.2

- Create virtaul ENV
([repoName])>>> python -m venv [myvenv]

- Activate/Deactivate your virtual ENV
([repoName])>>> [myvenv]\Scripts\activate - Activate your virtual ENV
([myvenv]).../([repoName])>>> [myvenv]\Scripts\activate - Activate your virtual ENV
([myvenv]).../([repoName])>>> [myvenv]\Scripts\deactivate - Deactivate your virtual ENV

- Create requirements.txt file in your basedir
([myvenv]).../([repoName])>>> type nul > [file_name.txt] - (for windows)
([myvenv]).../([repoName])>>> touch [file_name.txt] - (for MAC/Linux)


- Install Django 
([myvenv]).../([repoName])>>> pip install django

- make sure you have install django successfully in your virtual env
([myvenv]).../([repoName])>>> python -m django --version
5.1.5

- Get list modules and packages in your virtual env
([myvenv]).../([repoName])>>> pip list/pip freeze

- Installed moduels and packages add in requirements.txt
([myvenv]).../([repoName])>>> pip freeze > requirements.txt

- Install moduels and packages from requirements.txt file
([myvenv]).../([repoName])>>> pip install -r requirements.txt

- Now, Create your django project
([myvenv]).../([repoName])>>> django-admin startproject [projectName] .

- Create Django app
([myvenv]).../([repoName])>>> python manage.py startapp [appName]

- Install that app into the settings.py 
GO TO the project/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blogs' 
]

- migrations and makemigrations
([myvenv]).../([repoName])>>> python manage.py makemigrations
([myvenv]).../([repoName])>>> python manage.py migrate

- For show database dashboard Install VS code Extension "SQLite Viewer" and author name is "Florian Klampfer"

- run your django project
([myvenv]).../([repoName])>>> python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
January 28, 2025 - 10:51:15
Django version 5.1.5, using settings 'project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.


- Create superuser
([myvenv]).../([repoName])>>> python manage.py createsuperuser
Username (leave blank to use '[system-name]'): admin
Email address: admin
Error: Enter a valid email address.
Email address: admin@gmail.com
Password: ********
Password (again): ********
The password is too similar to the username.
This password is too short. It must contain at least 8 characters.
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.


- Setup MVT with URL

app/
    - models.py - file
    - views.py - file
    - urls.py [ manually create ] - file
    - templates [ create manually ] - dir
        - app [ create manually ] - dir
    - static [ create manually ] - dir
        - app [ create manually ] - dir


- Prepare Django form
s-1] <form action="" method="post" enctype="multipart/form-data">
s-2] {% csrf_token %}
s-3] make sure all input fields have name attribut with unique name
s-4] button type submit

- collect statci files in base dir:

([myvenv]).../([repoName])>>> python manage.py collectstatic


<!-- Send SMS -->

pip install twilio
------------------------------------------

from twilio.rest import Client

# Your Account SID and Auth Token from twilio.com/console
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

# Initialize the Twilio client
client = Client(account_sid, auth_token)

def send_sms(receiver_number, message_body):
    try:
        # Send SMS
        message = client.messages.create(
            body=message_body,
            from_='your_twilio_phone_number',
            to=receiver_number
        )
        print(f"Message sent successfully to {receiver_number}. SID: {message.sid}")
        return True
    except Exception as e:
        print(f"Failed to send SMS to {receiver_number}. Error: {str(e)}")
        return False

# Example usage
receiver_number = '+1234567890'  # Replace with the recipient's phone number
message_body = 'Hello from Twilio!'
send_sms(receiver_number, message_body)


<!-- Payment Gateway -->
s1] 
pip install razorpay

s2] Create a Razorpay Account and get your API keys from "Razorpay Dashboard".

Update settings.py

RAZORPAY_KEY_ID = "your_razorpay_key"
RAZORPAY_KEY_SECRET = "your_razorpay_secret"

s3] Create a Payment View in views.py
import razorpay
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

def initiate_payment(request):
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
    payment = client.order.create({
        "amount": 50000,  # Amount in paise (₹500)
        "currency": "INR",
        "payment_capture": "1"
    })
    return render(request, "payment.html", {"payment": payment})



4] Create payment.html with Razorpay Button

<script src="https://checkout.razorpay.com/v1/checkout.js"></script>
<button id="pay-btn">Pay Now</button>

<script>
    var options = {
        "key": "{{ payment.id }}",
        "amount": "50000",
        "currency": "INR",
        "name": "My Business",
        "description": "Test Payment",
        "handler": function (response){
            alert("Payment Successful! Payment ID: " + response.razorpay_payment_id);
        },
        "prefill": {
            "name": "John Doe",
            "email": "john@example.com"
        },
    };
    var rzp1 = new Razorpay(options);
    document.getElementById('pay-btn').onclick = function (e) {
        rzp1.open();
        e.preventDefault();
    }
</script>

<!-- Weather API -->

https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API%20key}

<!-- Email sending -->
s1] settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'samarthpatodekar@gmail.com'
EMAIL_HOST_PASSWORD = 'lielqdcgggiayefx'

s2] views.py

from django.core.mail import send_mail
from django.conf import settings

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

<!-- django-allauth -->

s1] pip install django-allauth

s2] settings.py

<!-- https://docs.allauth.org/en/latest/installation/quickstart.html -->
INSTALLED_APPS = [
    "django.contrib.sites",  # Required for django-allauth
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.facebook",
    "allauth.socialaccount.providers.instagram",
    "allauth.socialaccount.providers.github",
]

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

SITE_ID = 1

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

s3] python manage.py migrate

s4] Setup Google & Facebook OAuth Credentials

You need to create OAuth credentials for Google and Facebook.

(A) Google OAuth Setup
1] Go to Google Developers Console: Google Cloud Console
2] Create a new project and navigate to APIs & Services > Credentials.
3] Click on Create Credentials > OAuth Client ID.
4] Configure the OAuth consent screen (Set "Email" and "Profile" as scopes).
5] Choose Web Application and enter the redirect URI:
    http://localhost:8000/accounts/google/login/callback/
6] Copy the Client ID and Client Secret.

(B) Facebook OAuth Setup
1] Go to Facebook Developer Console: Facebook Developers
2] Create an App and navigate to Settings > Basic.
3] Under OAuth Settings, add the redirect URI:
    http://localhost:8000/accounts/facebook/login/callback/
4] Copy the App ID and App Secret.

s5] python manage.py runserver

s6] Add Login Buttons in HTML
Add Google and Facebook login buttons in your login.html:
<a href="{% provider_login_url 'google' %}?next=/">Login with Google</a>
<a href="{% provider_login_url 'facebook' %}?next=/">Login with Facebook</a>

<!-- GitHub API's -->

s1] pip install requests PyGithub

s2] 2. Get a GitHub Personal Access Token
1] Go to GitHub Developer Settings.
2] Click "Generate new token" (classic) or create a fine-grained token.
3] Select scopes (e.g., repo, read:user).
4] Copy and store your token securely.


s3] Configure settings.py
Store your GitHub token securely in settings.py:
GITHUB_ACCESS_TOKEN = "your_github_token_here"


s4] Fetch Data from GitHub API

import requests
from django.conf import settings
from django.http import JsonResponse

def get_github_repos(request, username):
    url = f"https://api.github.com/users/{username}/repos"
    headers = {"Authorization": f"token {settings.GITHUB_ACCESS_TOKEN}"}
    
    response = requests.get(url, headers=headers)
    data = response.json()
    
    return JsonResponse(data, safe=False)


s5] urls.py

from django.urls import path
from .views import get_github_repos

urlpatterns = [
    path("github/repos/<str:username>/", get_github_repos, name="github_repos"),
]

<!-- Google Maps API -->

Integrating Google Maps API in Django
You can use the Google Maps API in Django to display maps, get geolocation data, or calculate distances. Below are common use cases:

1️⃣ Displaying Google Maps in a Django Template
2️⃣ Fetching Latitude & Longitude (Geocoding API)
3️⃣ Calculating Distance Between Two Locations (Distance Matrix API)

1. Get a Google Maps API Key
    1] Go to Google Cloud Console
    2] Create a new project.
    3] Navigate to APIs & Services > Credentials.
    4] Click "Create Credentials" > "API Key".
    5] Enable the required APIs:
        - Maps JavaScript API
        - Geocoding API
        - Distance Matrix API (optional)
    6] Copy the API Key.

2. Store API Key in settings.py
Add your Google Maps API Key:
GOOGLE_MAPS_API_KEY = "your_google_maps_api_key_here"

3. Display Google Map in Django Template
Add this in your HTML template (maps.html):

<!DOCTYPE html>
<html>
<head>
    <title>Google Map in Django</title>
    <script src="https://maps.googleapis.com/maps/api/js?key={{ google_maps_api_key }}&callback=initMap" async defer></script>
    <script>
        function initMap() {
            var location = { lat: 37.7749, lng: -122.4194 };  // Example: San Francisco
            var map = new google.maps.Map(document.getElementById("map"), {
                zoom: 12,
                center: location,
            });
            new google.maps.Marker({
                position: location,
                map: map,
            });
        }
    </script>
</head>
<body>
    <h2>Google Map Example</h2>
    <div id="map" style="height: 500px; width: 100%;"></div>
</body>
</html>


Pass API Key from Django View (views.py):

from django.shortcuts import render
from django.conf import settings

def show_map(request):
    return render(request, "maps.html", {"google_maps_api_key": settings.GOOGLE_MAPS_API_KEY})

URL Route (urls.py):

from django.urls import path
from .views import show_map

urlpatterns = [
    path("map/", show_map, name="google_map"),
]


Test it in the browser:

http://127.0.0.1:8000/map/


4. Get Latitude & Longitude (Geocoding API)
You can convert an address to latitude & longitude using Google's Geocoding API.

View Function (views.py):

import requests
from django.conf import settings
from django.http import JsonResponse

def get_coordinates(request, address):
    url = f"https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": address,
        "key": settings.GOOGLE_MAPS_API_KEY,
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    if data["status"] == "OK":
        location = data["results"][0]["geometry"]["location"]
        return JsonResponse({"latitude": location["lat"], "longitude": location["lng"]})
    
    return JsonResponse({"error": "Invalid address"}, status=400)

URL Route (urls.py):
path("geocode/<str:address>/", get_coordinates, name="get_coordinates"),

Test it in the browser:
http://127.0.0.1:8000/geocode/New York/



5. Calculate Distance Between Two Locations
You can calculate the distance and travel time between two locations using Google Distance Matrix API.

View Function (views.py):
def get_distance(request, origin, destination):
    url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    params = {
        "origins": origin,
        "destinations": destination,
        "key": settings.GOOGLE_MAPS_API_KEY,
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    if data["status"] == "OK":
        element = data["rows"][0]["elements"][0]
        if element["status"] == "OK":
            distance = element["distance"]["text"]
            duration = element["duration"]["text"]
            return JsonResponse({"distance": distance, "duration": duration})
    
    return JsonResponse({"error": "Invalid locations"}, status=400)

URL Route (urls.py):
path("distance/<str:origin>/<str:destination>/", get_distance, name="get_distance"),

Test it in the browser:
http://127.0.0.1:8000/distance/New York/Los Angeles/

