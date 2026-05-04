from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import InputRequired, Email, Length, Optional


class RegisterForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[InputRequired(), Email(), Length(max=50)],
        description="Your school email address",
    )
    password = PasswordField("Password", validators=[InputRequired(), Length(min=4)])

    # EXERCISE 1: Role selection during registration
    role = SelectField(
        "Role",
        choices=[
            ("viewer", "Viewer - Can only view students"),
            ("admin", "Admin - Can add, edit, and delete students"),
        ],
        default="viewer",
        validators=[Optional()],
    )
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Login")


# EXERCISE 2: Profile form for image upload and display name
class ProfileForm(FlaskForm):
    display_name = StringField("Display Name", validators=[Optional(), Length(max=100)])
    profile_image = FileField(
        "Profile Picture",
        validators=[
            FileAllowed(
                ["jpg", "png", "jpeg"], "Only JPG, PNG, and JPEG images are allowed!"
            )
        ],
    )
    submit = SubmitField("Update Profile")
