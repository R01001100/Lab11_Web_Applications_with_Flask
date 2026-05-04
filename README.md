# 🌐 Lab 11 — Flask Web Applications

> **Activity 11 · Building Web Applications with Flask**  
> *Additional Exercises: Role-Based Access Control & Profile Management*

> Technological University of the Philippines – Manila | Electronics Engineering Department

---

## 📋 Overview

This project is the web implementation of the **Lab 11 – Building Web Applications with Flask** laboratory activity, including the **two additional exercises**. It demonstrates full-stack web development using Flask, featuring:

- **Exercise 1:** Role-Based Student Management System (Admin vs Viewer access control)
- **Exercise 2:** Profile Management with Image Upload functionality

The application was developed using Python, Flask, Flask-WTF, Flask-SQLAlchemy, Flask-Login, and follows a structured Flask project setup with reusable templates, static assets, and SQLite database support.

---

## 🌐 Live Demo

👉 **https://r01001100.github.io/Lab11_Web_Applications_with_Flask/**

> ⚠️ Note: The GitHub Pages version is only a frontend demo/mimic of the original Flask application. Since GitHub Pages only supports static files (HTML, CSS, and JavaScript), the deployed version recreates the interface and behavior using `index.html` instead of running the actual Python Flask backend.

---

## ✨ Features

### 🔐 User Authentication System
- User registration with email and password
- Secure password hashing using Werkzeug
- Login and logout functionality
- Session handling with Flask-Login
- Protected routes using `@login_required`

### 👨‍🎓 Exercise 1: Role-Based Student Management
- **Admin Role** – Full CRUD operations (add, view, delete students)
- **Viewer Role** – Read-only access to student list
- Role selection during registration
- Role-based conditional rendering in templates
- Permission checks on all student management routes

### 🖼️ Exercise 2: Profile Management with Image Upload
- Update display name (separate from email)
- Upload profile pictures (JPG, PNG, JPEG only)
- File validation (extension, size limit: 16MB)
- Secure filename generation with timestamps
- Automatic deletion of old profile images
- Dashboard displays uploaded profile picture and display name

### 🎨 Frontend and Template System
- Reusable layouts using template inheritance
- Navigation bar with conditional rendering based on login status
- Flash messages for user feedback
- External CSS styling with static assets
- Responsive design for mobile devices

### 🗄️ Database Integration
- SQLite database with SQLAlchemy ORM
- **User Model:** id, email, password, role, display_name, profile_image
- **Student Model:** id, full_name, email
- Automatic table creation with Flask application context

---

## 🛠️ Built With

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="60" alt="python logo"/>
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" height="60" alt="flask logo"/>
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" height="60" alt="sqlite logo"/>
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" height="60" alt="html5 logo"/>
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" height="60" alt="css3 logo"/>
</div>

---

## 📚 References

- Flask Documentation. https://flask.palletsprojects.com/
- SQLAlchemy Documentation. https://www.sqlalchemy.org/
- Miguel Grinberg. *Flask Web Development*
- Real Python. *Flask by Example*. https://realpython.com/flask-by-example-part-1-project-setup/
- FreeCodeCamp. *Flask Tutorial for Beginners*. https://www.youtube.com/watch?v=Z1RJmh_OqeA

---

## 👤 Author

**R01001100**  
TUP – Manila | BS Electronics Engineering
