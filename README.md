# Django_Admin_Portal

## Project Description:
This is a Django-based RESTful Project Management System designed to manage three core entities: Users, Clients, and Projects.

The system allows for:
  1. Registration and management of clients.  
  2. Creation and assignment of projects to specific clients and users.  
  3. User-specific project views based on authentication.  
  4. Complete CRUD operations for Clients and Projects.

The system uses Django's built-in admin for user management and Django REST Framework for building APIs, along with JWT for secure authentication.

---

## Features:
1. JWT (JSON Web Token) Authentication for Users.  
2. API endpoints for client registration, project creation, update, delete.  
3. Each project is tied to both a client and a user.  
4. Authenticated users can view only their assigned projects.  
5. Admin can manage all users, clients, and projects from the admin dashboard.

---

## Tech Stack:
1. Python 3.13  
2. Django 4.2  
3. Django REST Framework  
4. Simple JWT (for Authentication)  
5. MySQL Database  

---

## Setup Instructions
### 1️. Clone the Repository
```bash
git clone https://github.com/k-venky-reddy/Django_Admin_Portal.git
cd project-management-system
```
### 2️. Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```
### 3️. Install Dependencies

```bash
pip install -r requirements.txt
```
### 4️. Set Up MySQL Database

Create a database named `django` in your MySQL instance.
Then update `DATABASES` in `project_management/settings.py` as shown below:
```python
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
```
### 5️. Run Migrations
```bash
python manage.py makemigrations api
```
```bash
python manage.py migrate
```
### 6️. Create a Superuser
```bash
python manage.py createsuperuser
```
### 7️. Start the Development Server
```bash
python manage.py runserver
```
Now visit [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log in using your superuser credentials.
---

## Contact Me

Hi, I'm Venkatesh Reddy. I developed this project to demonstrate my skills in authentication, API design, and user-specific data handling.
If you need any further information or assistance, feel free to contact me.

- Reach me at: kvenkateshreddydataengineer@gmail.com
