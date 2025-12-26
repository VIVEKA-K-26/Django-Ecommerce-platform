# Django E-commerce Platform

## Objective
Develop a comprehensive e-commerce platform with CRUD operations, dynamic pricing, and advanced search features using Django.

---

## Tech Stack
- Backend: Python, Django
- Database: SQLite (can be replaced with PostgreSQL)
- Frontend: HTML, CSS
- Authentication: Django built-in User model
- Sessions & Cookies: Django sessions

---

## Features Implemented

### 1. CRUD Operations
- Products: Create, Read, Update, Delete
- Categories: Create, Read, Update, Delete
- Users: Managed using Django’s built-in User model

### 2. Dynamic Pricing
- Tracks user visits using Django sessions
- Applies a discount after multiple visits
- Pricing logic handled dynamically in views

### 3. Search & Filters
- Search by product name
- Search by category
- Filter by price range
- Auto-suggestion-ready backend logic

### 4. Admin Panel
- Superuser access
- Manage users, products, and categories

---

## Project Structure


## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/django-ecommerce-platform.git
cd django-ecommerce-platform

### 2. Create virtual environment 

python -m venv venv
venv\Scripts\activate

### 3.Install dependencies

pip install django

### 4.Run migrations

python manage.py makemigrations
python manage.py migrate

### 5.Create superuser

python manage.py createsuperuser

### 6.Run server

python manage.py runserver


