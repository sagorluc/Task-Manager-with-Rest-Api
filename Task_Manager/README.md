# Task Manager with REST API

This project is a task management web application with a REST API built using Django. It allows multiple users to create, view, update, and delete tasks. The application uses Django templates for rendering views, PostgreSQL for the database, and Django ORM for managing database relations.

## Getting Started

### Prerequisites

- Python 3.10.9
- PostgreSQL
- Git

## Installation

### Clone the repository:

* git clone https://github.com/sagorluc/Task-Manager-with-Rest-Api.git
* cd Task-Manager-with-Rest-Api


### Create a virtual environment:
virtualenv vrenv

.\vrenv\Scripts\activate

### Install the project dependencies:
pip install -r requirements.txt

### Create a new PostgreSQL database:
* psql -U postgres
* CREATE DATABASE task_manager;
* CREATE USER sagor WITH PASSWORD '102030';
* GRANT ALL PRIVILEGES ON DATABASE task_manager TO sagor;

### Set up environment variables:
* pip install python-dotenv
* SECRET_KEY = os.environ.get('SECRET_KEY')

### Apply migrations and create a superuser:
* python manage.py makemigrations
* python manage.py migrate
* python manage.py createsuperuser

### Run the development server:
python manage.py runserver

# Features
* User Authentication (Registration, Login)
* Password Reset (Optional)
* Task List View
* Task Creation View
* Task Details View (Multiple image can set for one task and can delete the particular image)
* Task Update View (with image)
* Task Deletion (with confirmation)
* Filtering and Searching tasks
* REST API endpoints for task Create, Update, Retrieve, Delete

# Django Template Documentation URL
* Registration Or Sign up: http://127.0.0.1:8000/auth/
* Login: http://127.0.0.1:8000/auth/login/
 

# REST API Documentation
### List all tasks
* Endpoint: /api/ <br>
* Method: GET

# Retrieve a single task
* Endpoint: /api/tasks/<task_id>/
* Method: GET

# Create a new task
* Endpoint: /api/
* Method: POST

# Update an existing task
* Endpoint: /api/tasks/<task_id>/
* Method: PUT or PATCH

# Delete a task
* Endpoint: /api/tasks/<task_id>/
* Method: DELETE

# Acknowledgments
* [Django Documentation]('https://docs.djangoproject.com/en/3.2/')
* [Django Rest Framework Documentation]('https://www.django-rest-framework.org/')
* [PostgreSQL Documentation]('https://www.postgresql.org/docs/')
* [Git Documentation]('https://git-scm.com/doc')

# Contributors
* [Md. Sagar Ali]('https://www.linkedin.com/in/mdsagarali/')