mkdir project
cd project

python -m venv env

.\env\Scripts\activate

pip install django djangorestframework

django-admin startproject myproject

python manage.py startapp myapp

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver
