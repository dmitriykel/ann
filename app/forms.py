from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField, FileRequired


class UploadImageForm(FlaskForm):
    image = FileField('Upload your image', validators=[FileRequired()])
    submit = SubmitField('Upload')
