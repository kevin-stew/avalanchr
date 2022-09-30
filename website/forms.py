from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired, Email, InputRequired, EqualTo

class UserLoginForm(FlaskForm):
    # email, password, submit_button
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators= [InputRequired()])
    submit_button = SubmitField()

class UserSignupForm(FlaskForm):
    # email, password, submit_button
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators= [InputRequired(),EqualTo("confirm", message = 'Make sure...')])
    confirm = PasswordField('Repeat Password')
    submit_button = SubmitField()

class ObjectUploadForm(FlaskForm):
    title = StringField('Title', validators = [DataRequired()])
    description = TextAreaField('Description')
    price = StringField('Price', validators = [DataRequired()])
    dimensions = StringField('Dimensions')
    weight = StringField('Weight')
    img_url = FileField('Preview image', validators = [DataRequired()])  
    model_url = FileField('3D model file', validators = [DataRequired()])
    # img_url = StringField('Preview image', validators = [DataRequired()])  
    # model_url = StringField('3D model file', validators = [DataRequired()])
    submit_button = SubmitField()