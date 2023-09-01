# Welcome to MzaziConnect Backend

This repository contains the backend code for a RESTful APIs that provides access to assignments  resources for teachers in the Competency Based Curriculum.


The README file provides the  instructions on how to set up and run a Django application. It covers installing `pip`, setting up a virtual environment, installing dependencies from `requirements.txt`, and running the Django app.

## Prerequisites

Ensure you have the following installed on your system:

- `Python 3.10.12`
- `pip` (Python package installer)

## Step 1: Install `pip`

1. Open a terminal.
2. Run the following command to update package lists:

   ```
   sudo apt update
   ```

3. Install `pip` using the following command:

   ```
   sudo apt install python3-pip
   ```

## Step 2: Set Up a Virtual Environment

1. Open the terminal.
2. Navigate to the directory where you want to create your Django project.

   ```
   cd directory-name
   ```
3. Run the following command to create a virtual environment:

   ```
   python -m venv myenv
   ```

4. Activate the virtual environment:

   ```
   source myenv/bin/activate
   ```
5. Install packages using pip:

   ```
   $ pip install django
   ```
6. Check installed packages:

   ```
   $ pip freeze
   ```


## Step 3: Install Dependencies and Run the App

1. Save installed packages to a requirements file:

   ```
   $ pip freeze > requirements.txt
   ```

2. Create a new Django project:

   ```
   django-admin startproject myproject
   ```

   This will create a directory named `myproject` containing the initial project files.

3. Navigate into the project directory:

   ```
   cd myproject
   ```

4. Run database migrations:

   ```
   python manage.py migrate
   ```

5. Create a superuser to access the Django admin dashboard:

   ```
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```
   python manage.py runserver
   ```

   The server starts, navigate to `http://127.0.0.1:8000/` in your browser.