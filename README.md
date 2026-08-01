# 🎂 Cake Shop - Django Web Application

Welcome to the **Cake Shop** project! This repository is a Django-based web application designed as a teaching resource to help students understand Django development, web architectures (MVT/MVC pattern), database CRUD operations, and session handling.

This project is divided into two primary modules:
1. **Customer Portal (`customerapp`)**: Allows users to register, log in, browse available cakes by categories, and manage their cart.
2. **Admin Portal (`adminapp`)**: Allows admins to monitor registered customers, manage customer accounts (edit/delete), and manage the product catalog (add new cakes with images).

---

## 🚀 Quick Start Guide

Follow these step-by-step instructions to clone, set up, and run the project locally on your machine.

### Prerequisites
Make sure you have the following installed:
* [Python 3.10+](https://www.python.org/downloads/)
* [Git](https://git-scm.com/)

---

### Step 1: Clone the Repository
Clone this repository to your local system and navigate to the project directory:
```bash
git clone https://github.com/sujithtr24/cakeshop_slot2.git
cd cakeshop_slot2
```

---

### Step 2: Set Up a Virtual Environment (Recommended)
A virtual environment keeps the project dependencies isolated.

* **On Windows (PowerShell/CMD):**
  ```powershell
  python -m venv env
  .\env\Scripts\activate
  ```
* **On macOS / Linux:**
  ```bash
  python3 -m venv env
  source env/bin/activate
  ```

Once activated, your terminal prompt should display `(env)`.

---

### Step 3: Install Required Dependencies
Install the required packages using pip:
```bash
pip install -r requirements.txt
```

*(Note: The project uses **Django 6.0.6** and basic database helpers like **sqlparse** and **tzdata**).*

---

### Step 4: Run Database Migrations
Create the database tables in SQLite based on the models defined in the apps:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

### Step 5: Create an Admin Superuser
To access the built-in Django Admin Interface at `/admin/`, create a superuser account:
```bash
python manage.py createsuperuser
```
Follow the prompts in the terminal to set a username, email, and password.

---

### Step 6: Start the Development Server
Launch the Django local development server:
```bash
python manage.py runserver
```

Once started, open your web browser and go to: **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 🌐 Application URL Reference

Use these endpoints to navigate the project:

### Customer Portal (`customerapp`)
* **Home Page:** `http://127.0.0.1:8000/customer/home-page/`
* **Register Page:** `http://127.0.0.1:8000/customer/register-page/`
* **Login Page:** `http://127.0.0.1:8000/customer/login-page/`
* **View Cakes/Products:** `http://127.0.0.1:8000/customer/view-products/`

### Admin Portal (`adminapp`)
* **Admin Dashboard:** `http://127.0.0.1:8000/adminapp/admin-dashboard/`
* **Manage Products:** `http://127.0.0.1:8000/adminapp/products/`
* **Add New Product:** `http://127.0.0.1:8000/adminapp/add-product`
* **Manage Customers:** `http://127.0.0.1:8000/adminapp/customers/`

### Built-in Django Admin
* **Django Admin:** `http://127.0.0.1:8000/admin/`

---

## 📂 Project Structure

Here is a quick overview of the key directories and files in this repository:

```text
cakeshop_slot2/
│
├── cakeshop/              # Core project settings, main routing (urls.py), and configuration
├── customerapp/           # Customer portal: models, views, templates mapping, and URLs
├── adminapp/              # Admin portal: models, views, and templates mapping
├── templates/             # HTML Templates (organized for frontend & admin views)
├── static/                # Static assets (CSS, JS, Fonts, Images)
├── media/                 # Media directory for user/admin uploaded files (e.g., cake images)
├── manage.py              # Django's command-line utility
├── db.sqlite3             # SQLite Database (contains default development schema/data)
└── requirements.txt       # List of Python library dependencies
```

---

## 🛠️ Key Topics for Students to Explore
1. **Models and Relationships**: Look at how `customerapp/models.py` uses `models.ForeignKey` to reference `adminapp/models.py` (Connecting a Cart item to a Customer and a Cake).
2. **Session Management**: Review the `login_page` view in `customerapp/views.py` to see how user login session data (`request.session['user_id']`) is set.
3. **Form Handling and HTTP POST Requests**: Inspect the `adminAddProducts` view in `adminapp/views.py` to see how form input values and files (`request.FILES`) are processed and saved.
4. **Media and Static Settings**: Understand how `settings.MEDIA_URL` and `settings.MEDIA_ROOT` are configured in `settings.py` and linked in `cakeshop/urls.py` to serve uploaded images.
