from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return f"<User {self.email}>"


class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)

    def __repr__(self):
        return f"<Student {self.full_name}>"


# Try It: Add and Display a Sample Student (to run in notebook)
# with app.app_context():
#     sample_student = Student(full_name="Maria Santos", email="maria@example.com")
#     db.session.add(sample_student)
#     db.session.commit()
#     all_students = Student.query.all()
#     for s in all_students:
#         print(f"{s.id}: {s.full_name} ({s.email})")
