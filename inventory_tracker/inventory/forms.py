from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, IntegerField, SubmitField, TextAreaField, DecimalField
from wtforms.validators import DataRequired, Length


# When using forms we need to set a secret key.
# It will protect the application from modifying cookies, cross site requests, forgary attacks

class ItemForm(FlaskForm):
    name = StringField('Item Name', validators=[DataRequired(), Length(min=2, max=20)])
    manufacturer = StringField('Manufacturer', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    summary = StringField('Summary', validators=[DataRequired(), Length(min=2, max=100)])
    description = TextAreaField('Description')
    unit_price = DecimalField('Unit Price', validators=[DataRequired()])
    retail_price = DecimalField('Retail Price', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired(), Length(min=2, max=20)])

    image = FileField('Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField("Submit")
