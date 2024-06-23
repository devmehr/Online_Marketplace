# Online Marketplace

Welcome to the Online Marketplace project! This Django application is designed to facilitate the buying and selling of goods and services between users. This README file will guide you through the setup and usage of the project.

# Table of Contents

- Features
- Installation
- Configuration
- Usage
- Testing
- Contributing
- License

# Features

- User authentication and authorization
- Product listing with categories and tags
- Shopping cart and checkout system
- Order management for users and administrators
- Payment integration with Stripe
- Review and rating system for products
- Search functionality for products
- Responsive design for mobile and desktop users

# Installation

## Prerequisites

- Python 3.10.12
- Django 5.0.6

## Step-by-Step Guide

1. **Clone the repository:**

    git clone https://github.com/devmehr/Online_Marketplace
    cd online-marketplace

2. **Create a virtual environment:**

    python3 -m venv online_market
    source online_market/bin/activate

3. **Install the required dependencies:**

    pip install -r requirements.txt

4. **Configure your database settings in `settings.py`.**

    If you are using PostgreSQL, update the `DATABASES` setting with your database credentials. For a simple setup, you can use SQLite (default configuration).

5. **Run database migrations:**

    python manage.py migrate

6. **Create a superuser:**

    python manage.py createsuperuser

7. **Start the development server:**

    python manage.py runserver

# Configuration

Configuration settings can be found and modified in the `settings.py` file located in the project directory. This includes database settings, installed apps, middleware, static files, and more.

# Usage

Once the development server is running, you can access the application by navigating to `http://127.0.0.1:8000/` in your web browser.

## Installed Apps

### Core

The core app contains the base functionality and models used across the project, including user authentication and authorization.

### Dashboard

The dashboard app provides administrative functionality, allowing users to manage products, orders, and user accounts.

### Conversation

The conversation app facilitates communication between buyers and sellers through messaging.

### Item

The item app handles product listings, including adding, editing, and deleting products. Users can also search for products, view product details, and leave reviews and ratings.

# Testing

To run the test suite, execute the following command:

python manage.py test

This will run the tests defined in each app's `tests.py` file.

# Contributing

We welcome contributions to the Online Marketplace project! To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Implement your changes and commit them with descriptive messages.
4. Push your branch to your forked repository.
5. Open a pull request to the `main` branch of the original repository.

Please ensure your code adheres to the project's coding standards and includes relevant tests.

# License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

