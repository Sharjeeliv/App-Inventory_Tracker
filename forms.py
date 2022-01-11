from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, IntegerField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


# When using forms we need to set a secret key.
# It will protect the application from modifying cookies, cross site requests, forgary attacks

class ItemForm(FlaskForm):
    name = StringField('Item Name', validators=[DataRequired(), Length(min=2, max=20)])
    manufacturer = StringField('Manufacturer', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    summary = StringField('Summary', validators=[DataRequired()])
    image = FileField('Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField("Submit")
