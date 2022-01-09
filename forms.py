from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


# When using forms we need to set a secret key.
# It will protect the application from modifying cookies, cross site requests, forgary attacks

class NewItemForm(FlaskForm):
    name = StringField('Item Name', validators=[DataRequired(), Length(min=2, max=20)])
    manufacturer = StringField('Manufacturer', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    summary = StringField('Summary', validators=[DataRequired()])
    submit = SubmitField("Create Item")


class UpdateItemForm(FlaskForm):
    name = StringField('Item Name', validators=[DataRequired(), Length(min=2, max=20)])
    manufacturer = StringField('Manufacturer', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    summary = TextAreaField('Summary', validators=[DataRequired()])
    submit = SubmitField("Update Item")
