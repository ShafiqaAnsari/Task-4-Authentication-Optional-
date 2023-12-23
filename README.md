# Task-4-Authentication-Optional-
1. Django: Implement token-based authentication using Django REST framework.

#step to run this project

1. Open this folder in Visual Studio Code or Pycharm
2. Open a terminal or command prompt and navigate to the directory where your Django project is located.
     cd path/project
3. install the necessary packages that are used in this project. Run the below commands in terminal to install packages
     pip install django
     pip install djangorestframework    
     pip install django-filter
4. perform the migration by running the below command in cmd
     python manage.py migrate
5. to run the this project run the below command python manage.py runserver
6. Open your web browser and go to http://127.0.0.1:8000/bookapi/
7. It will show you this because you are not the autheticate user. 
   {
    "detail": "Authentication credentials were not provided."
   }

