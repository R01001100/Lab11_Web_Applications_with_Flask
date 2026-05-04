from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)

    # EXERCISE 1: Role-Based Student Management
    role = db.Column(db.String(20), nullable=False, default="viewer")

    # EXERCISE 2: Profile Management with Image Upload
    display_name = db.Column(db.String(100), nullable=True)
    profile_image = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f"<User {self.email} ({self.role})>"

    # EXERCISE 1: Helper method for role checking
    def is_admin(self):
        return self.role == "admin"


class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)

    def __repr__(self):
        return f"<Student {self.full_name}>"
