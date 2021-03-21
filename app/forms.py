from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email  

class PropertyForm(FlaskForm):
    name = StringField('Property Title', validators = [DataRequired()])
    nobed = StringField('No. of Rooms', validators = [DataRequired()])
    nobath = StringField('No. of Bathrooms', validators = [DataRequired()])
    location = StringField('Location', validators = [DataRequired()])
    price = StringField('Price', validators = [DataRequired()])
    type = SelectField(u'Type', choices=['House','Apartment'], validators= [DataRequired()])
    description = TextAreaField('Description', validators = [DataRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'], "Please check format, only PNG and JPG images are allowed!")])