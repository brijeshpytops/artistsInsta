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