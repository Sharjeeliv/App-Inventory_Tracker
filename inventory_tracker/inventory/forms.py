from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, IntegerField, SubmitField, TextAreaField, DecimalField
from wtforms.validators import DataRequired, Length


class ItemForm(FlaskForm):
    """
    A secret key is required to use several features such as flash. It will protect this application
    from Cross-Site Request Forgery (CSRF). WTForms is used to create and handle everything regarding
    forms for this application. It has built in validators and is simple to implement in HTML.

    One item form is used for the creation and updating of item entries in the inventory
    """

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
