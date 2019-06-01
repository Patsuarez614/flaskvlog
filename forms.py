from flask_wtf import Flaskform
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
	username = StringField('username', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_pw = PasswordField ('Confirm Password', validators=[DataRequired(), EqualTo ('password')])

	__init__(self, arg):
		super(RegistrationForm,FlaskForm._
		_init__()
		self.arg = arg
  