from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField


class UserRegisterForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    email = StringField('E-mail', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm_password', message="Field must be equal to Confirm password"),
    ])
    confirm_password = PasswordField('Confirm password', [
        validators.DataRequired(),
        validators.EqualTo('password', message='Field must be equal to Password'),
    ])
    submit = SubmitField('Register')
