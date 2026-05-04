from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import (
    LoginManager,
    login_user,
    login_required,
    logout_user,
    current_user,
)
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from forms import RegisterForm, LoginForm, ProfileForm
from models import db, User, Student
import os
from datetime import datetime

app = Flask(__name__, instance_relative_config=True)

app.config["SECRET_KEY"] = "my-secret-key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    app.instance_path, "app.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# EXERCISE 2: Upload configuration for profile images
UPLOAD_FOLDER = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "static", "uploads"
)
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16MB max

# Create upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

db.init_app(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Helper function for EXERCISE 2: File validation
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


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
        # Check if email already exists
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash("Email already registered.")
            return redirect(url_for("register"))

        hashed_pw = generate_password_hash(form.password.data)

        #  EXERCISE 1: Get role from form
        role = form.role.data if form.role.data else "viewer"

        user = User(email=form.email.data, password=hashed_pw, role=role)
        db.session.add(user)
        db.session.commit()
        flash(f"Registration successful! Your role is: {role}")
        return redirect(url_for("login"))
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            # EXERCISE 1: Show role on login
            flash(f"Logged in successfully as {user.role}.")
            # EXERCISE 2: Redirect to dashboard instead of students
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid email or password.")
    return render_template("login.html", form=form)


# EXERCISE 2: Dashboard route to show user profile
@app.route("/dashboard")
@login_required
def dashboard():
    # Get student count for stats
    student_count = Student.query.count()
    return render_template(
        "dashboard.html", user=current_user, students_count=student_count
    )


# EXERCISE 2: Profile management with image upload
@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    form = ProfileForm()

    if form.validate_on_submit():
        # Update display name
        if form.display_name.data:
            current_user.display_name = form.display_name.data

        # Handle image upload
        if form.profile_image.data:
            file = form.profile_image.data
            if file and allowed_file(file.filename):
                # Secure filename and add timestamp to avoid duplicates
                filename = secure_filename(file.filename)
                unique_filename = (
                    f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{filename}"
                )
                filepath = os.path.join(app.config["UPLOAD_FOLDER"], unique_filename)
                file.save(filepath)

                # Delete old image if exists
                if current_user.profile_image:
                    old_path = os.path.join(
                        app.config["UPLOAD_FOLDER"], current_user.profile_image
                    )
                    if os.path.exists(old_path):
                        os.remove(old_path)

                current_user.profile_image = unique_filename
                flash("Profile picture uploaded successfully!")

        db.session.commit()
        flash("Profile updated successfully!")
        return redirect(url_for("dashboard"))

    return render_template("profile.html", form=form, user=current_user)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for("home"))


# EXERCISE 1: Students route with role-based access
@app.route("/students")
@login_required
def students():
    student_list = Student.query.order_by(Student.full_name).all()
    # Determine what to show based on role
    is_admin = current_user.is_admin()

    return render_template("students.html", students=student_list, is_admin=is_admin)


# EXERCISE 1: Add student - only admin can access
@app.route("/add-student", methods=["POST"])
@login_required
def add_student():
    # Only admin can add students
    if not current_user.is_admin():
        flash("Permission denied. Only administrators can add students.")
        return redirect(url_for("students"))

    name = request.form.get("name")
    email = request.form.get("email")

    if not name or not email:
        flash("Name and email are required.")
        return redirect(url_for("students"))

    # Check if student already exists
    existing = Student.query.filter_by(email=email).first()
    if existing:
        flash("A student with this email already exists.")
        return redirect(url_for("students"))

    student = Student(full_name=name, email=email)
    db.session.add(student)
    db.session.commit()
    flash("Student added successfully!")
    return redirect(url_for("students"))


# EXERCISE 1: Delete student - only admin can access
@app.route("/delete-student/<int:id>")
@login_required
def delete_student(id):
    # Only admin can delete students
    if not current_user.is_admin():
        flash("Permission denied. Only administrators can delete students.")
        return redirect(url_for("students"))

    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    flash("Student deleted successfully!")
    return redirect(url_for("students"))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    if not os.path.exists(os.path.join(app.instance_path, "app.db")):
        os.makedirs(app.instance_path, exist_ok=True)
    with app.app_context():
        db.create_all()
        # EXERCISE 1 & 2: Create default admin account
        if not User.query.filter_by(email="admin@tup.edu.ph").first():
            admin_user = User(
                email="admin@tup.edu.ph",
                password=generate_password_hash("admin123"),
                role="admin",
                display_name="Administrator",
            )
            db.session.add(admin_user)
            db.session.commit()
            print("=" * 50)
            print("Default admin created for testing:")
            print("Email: admin@tup.edu.ph")
            print("Password: admin123")
            print("=" * 50)
    app.run(debug=True)
