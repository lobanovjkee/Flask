from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField


class UserLoginForm(FlaskForm):
    email = StringField('E-mail', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired()])
    submit = SubmitField('Login')
