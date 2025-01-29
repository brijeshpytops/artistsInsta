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