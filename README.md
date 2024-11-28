# E-Commerce Django Project

This project sets up a simple e-commerce application with Customer and Order models.

## Setting Up the Environment

1. **Create a Virtual Environment and running it:**
    Creating command: python -m venv .venv
    Running command: .\.venv\Scripts\activate.ps1


2. **Installing Django:**
    pip install django

3. **Create Project:**
    django-admin startproject E_commerce
    cd E_commerce


4. **Create App (Customer and order):**
    python manage.py startapp Customer
    python manage.py startapp order
    - Update `INSTALLED_APPS` in `E_commerce/settings.py` to include your order and Customer.

## Running the Project

1. **Apply Migrations:**
    python manage.py makemigrations  # Create migrations
    python manage.py migrate         # Apply migrations to database


2. **Start Development Server:**

    python manage.py runserver

    Open http://127.0.0.1: