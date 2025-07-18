# Django_Admin_Portal
Project Description:
This is a Django-based RESTful Project Management System designed to manage three core entities: Users, Clients, and Projects. 
The system allows for:
        --> Registration and management of clients.
        --> Creation and assignment of projects to specific clients and users.
        --> User-specific project views based on authentication.
        --> Complete CRUD operations for Clients and Projects.
The system uses Djangos built-in admin for user management and Django REST Framework for building APIs, along with JWT for secure authentication.

Features: 
o	JWT (JSON Web Token) Authentication for Users.
o	API endpoints for client registration, project creation, update, delete.
o	Each project is tied to both a client and a user.
o	Authenticated users can view only their assigned projects.
o	Admin can manage all users, clients, and projects from the admin dashboard.

Tech Stack:
Python 3.13+
o	Django 4.2+
o	Django REST Framework
o	Simple JWT (for Authentication)
o	MySQL Database

1️ Clone the Repository
bash
git clone https://github.com/your-username/project-management-system.git
cd project-management-system

2️ Create and Activate Virtual Environment
bash
python -m venv venv
venv\Scripts\activate  # On Windows

3 Install Dependencies
bash
pip install -r requirements.txt

4️ Set Up MySQL Database
Create a database named django in your MySQL instance.
Then update DATABASES in project_management/settings.py:
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'root',
        'PASSWORD': 'your-password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

5️ Run Migrations
bash
python manage.py makemigrations api --> If Any Changes happens in Appi After completion Run this command Everything will be changed 
python manage.py migrate --> After Run This Command only will get the data in Database

6️ Create a Superuser
bash
python manage.py createsuperuser --> SuperUser Creation 

7️ Start the Development Server
bash
python manage.py runserver
Visit: http://127.0.0.1:8000/admin/ to log in with your superuser credentials.
