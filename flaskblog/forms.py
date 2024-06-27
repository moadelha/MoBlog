from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User # umport the user to check if it already exists in the db


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign up')

    def validate_username(self, username): #to check if user already exists in the db
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('User name already exists choose another ')
        
    def validate_email(self, email): #to check if email already exists in the db
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exists choose another ')
        
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')