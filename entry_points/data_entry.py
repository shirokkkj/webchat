from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import Length, DataRequired, EqualTo
    
class Register(FlaskForm):
    name = StringField('Name Account', validators=[Length(min=5, max=24), DataRequired()])
    password = PasswordField('Password', validators=[Length(min=3, max=10), DataRequired(), EqualTo('repeat_password', message='Password must be matchs')])
    repeat_password = PasswordField('Repeat your password', validators=[DataRequired()])
    submit = SubmitField('Register')
    
    
class File(FlaskForm):
    file = FileField('Image', validators=[FileAllowed(['jpg', 'png', 'Images Only'])])