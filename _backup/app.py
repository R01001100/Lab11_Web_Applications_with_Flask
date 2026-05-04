from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager,
    login_user,
    login_required,
    logout_user,
    current_user,
)
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegisterForm, LoginForm
from models import db, User, Student
import os

app = Flask(__name__, instance_relative_config=True)

# Debug logs
current_working_directory = os.getcwd()
static_folder_path = app.static_folder
print(f"DEBUG: Current working directory: {current_working_directory}")
print(f"DEBUG: Flask static folder: {static_folder_path}")
print(f"DEBUG: Does static folder exist? {os.path.isdir(static_folder_path)}")

css_file_path = os.path.join(static_folder_path, "css", "style.css")
image_file_path = os.path.join(static_folder_path, "images", "TUP.png")
print(f"DEBUG: Expected style.css path: {css_file_path}")
print(f"DEBUG: Does style.css exist? {os.path.exists(css_file_path)}")
print(f"DEBUG: Expected TUP.png path: {image_file_path}")
print(f"DEBUG: Does TUP.png exist? {os.path.exists(image_file_path)}")

# Config
app.config["SECRET_KEY"] = "my-secret-key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    app.instance_path, "app.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Init extensions
db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Routes
# Try It: Customize home.html with name and section
@app.route("/")
def home():
    return render_template("home.html", name="Ruselle Laude", section="BSECE 1C")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_pw = generate_password_hash(form.password.data)
        user = User(email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash("Registration successful!")
        return redirect(url_for("login"))
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Logged in successfully.")
            return redirect(url_for("students"))
        else:
            flash("Invalid email or password.")
    return render_template("login.html", form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for("home"))


@app.route("/students")
@login_required
def students():
    # Sort Students Alphabetically Before Displaying
    student_list = Student.query.order_by(Student.full_name).all()
    return render_template("students.html", students=student_list)


@app.route("/add-student", methods=["POST"])
@login_required
def add_student():
    name = request.form["name"]
    email = request.form["email"]
    student = Student(full_name=name, email=email)
    db.session.add(student)
    db.session.commit()
    return redirect(url_for("students"))


@app.route("/delete-student/<int:id>")
@login_required
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for("students"))


# Try It: Add 404 Error Handler to app.py
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    if not os.path.exists(os.path.join(app.instance_path, "app.db")):
        os.makedirs(app.instance_path, exist_ok=True)
        with app.app_context():
            db.create_all()
    app.run(debug=True)
