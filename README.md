# 🌐 Lab 11 — Flask Web Applications

> **Activity 11 · Building Web Applications with Flask**  

> Technological University of the Philippines – Manila | Electronics Engineering Department

---

## 📋 Overview

This project is the web implementation of the **Lab 11 – Building Web Applications with Flask** laboratory activity. It demonstrates the fundamentals of full-stack web development using Flask, including routing, template rendering, form validation, database integration, and user authentication.

The application was developed using Python, Flask, Flask-WTF, Flask-SQLAlchemy, and Flask-Login. It follows a structured Flask project setup with reusable templates, static assets, and SQLite database support.

---

## 🌐 Live Demo

👉 **https://r01001100.github.io/Lab11_Web_Applications_with_Flask/**

> ⚠️ Note: The GitHub Pages version is only a frontend demo/mimic of the original Flask application. Since GitHub Pages only supports static files (HTML, CSS, and JavaScript), the deployed version recreates the interface and behavior using `index.html` instead of running the actual Python Flask backend.

---

## 🌐 Features

### 1. 🔐 User Authentication System
- User registration with email and password
- Secure password hashing using Werkzeug
- Login and logout functionality
- Session handling with Flask-Login
- Protected routes using `@login_required`

### 2. 👨‍🎓 Student Management System
- Add student records through a web form
- Display all students stored in the database
- Delete existing student records
- Dynamic rendering using Jinja2 templates
- Database persistence using SQLite

### 3. 🎨 Frontend and Template System
- Reusable layouts using template inheritance
- Navigation bar with conditional rendering
- Flash messages for login and registration status
- External CSS styling with static assets
- Image support using Flask static folders

### 4. 🗄️ Database Integration
- SQLite database with SQLAlchemy ORM
- Separate models for Users and Students
- Automatic table creation with Flask application context
- Querying, inserting, and deleting records dynamically

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