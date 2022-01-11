from flask import Blueprint, render_template, flash, redirect, url_for
from forms import NewItemForm, UpdateItemForm
from models import Items
from app import db

routes = Blueprint("routes", __name__)


@routes.route('/')
@routes.route('/home')
def home():
    inventory = Items.query.all()
    return render_template('homepage.html', inventory=inventory)


@routes.route('/new-item', methods=['GET', 'POST'])
def new_item():
    form = NewItemForm()
    if form.validate_on_submit():
        item = Items(name=form.name.data, manufacturer=form.manufacturer.data, quantity=form.quantity.data,
                     summary=form.summary.data)
        db.session.add(item)
        db.session.commit()
        flash(f'Item entry for {form.name.data} created!', 'success')
        return redirect(url_for('routes.home'))
    return render_template('newitem.html', form=form)


@routes.route('/update_item/<int:item_id>')
def update_item(item_id):
    item = Items.query.get_or_404(item_id) # Get post with this id or get 404 meaning page does not exist
    return render_template('item.html', item=item)
