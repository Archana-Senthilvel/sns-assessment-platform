# SNS Assessment Platform

# Overview

The SNS Assessment Platform is a comprehensive solution designed to streamline the process of conducting and managing assessments. This platform is tailored to educational institutions, organizations, and training centers that require an efficient and scalable solution for managing quizzes, exams, and evaluations.


# How It Works

1. Admin Role:

Manage users and assign roles.

Configure platform settings.

2. Instructor Role:

Create assessments with various question types (MCQs, descriptive, etc.).

Monitor student performance.

3. Student Role:

Take assessments assigned by instructors.

View results and feedback.

# Installation and Setup

# Prerequisites

Python 3.8 or higher

pip (Python package manager)

A supported database (e.g., SQLite, MySQL, or PostgreSQL)

# Steps

1.Clone the Repository:

git clone <repository-url>
cd sns-assessment-platform-main

2.Install Dependencies:

pip install -r requirements.txt

3.Set Up the Database:

Configure the database connection in the settings file (e.g., config.py or .env).

4.Apply migrations to initialize the database:

python manage.py migrate

5.Run the Application:

python manage.py runserver

6.Access the Application:
Open your web browser and navigate to http://localhost:8000.
