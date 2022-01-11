from flask import Blueprint, render_template, flash, redirect, url_for, request, current_app
from forms import ItemForm
from models import Items
from app import db
import secrets
import os
from PIL import Image

routes = Blueprint("routes", __name__)


@routes.route('/')
@routes.route('/home')
def home():
    inventory = Items.query.all()
    return render_template('homepage.html', inventory=inventory)


@routes.route('/new', methods=['GET', 'POST'])
def new_item():
    form = ItemForm()
    if form.validate_on_submit():
        item = Items(name=form.name.data, manufacturer=form.manufacturer.data, quantity=form.quantity.data,
                     summary=form.summary.data)

        if form.image.data:
            picture_file = save_image(form.image.data)
            image = picture_file
            item.image = image

        db.session.add(item)
        db.session.commit()
        flash(f'Item entry for {form.name.data} created!', 'success')
        return redirect(url_for('routes.home'))
    return render_template('item_form.html', form=form, legend='New Item Form')


@routes.route('/item/<int:item_id>', methods=['GET', 'POST'])
def view_item(item_id):
    item = Items.query.get_or_404(item_id)
    image = url_for('static', filename='item_images/' + item.image)
    return render_template('item_view.html', item=item, legend='Update Item Form', image=image)


def save_image(picture_form):  # we make a random hex study this method
    random_hex = secrets.token_hex(8)
    _, ext = os.path.splitext(picture_form.filename)
    image_fn = random_hex + ext
    picture_path = os.path.join(current_app.root_path, 'static/item_images', image_fn)
    # resize
    output_size = (480, 480)
    i = Image.open(picture_form)
    i.thumbnail(output_size)
    i.save(picture_path)
    return image_fn


def delete_image(current):
    if current != 'default.jpg':
        picture_path = os.path.join(current_app.root_path, 'static/item_images', current)
        os.remove(picture_path)


@routes.route('/update/<int:item_id>', methods=['GET', 'POST'])
def update_item(item_id):
    item = Items.query.get_or_404(item_id)  # Get post with this id or get 404 meaning page does not exist
    form = ItemForm()
    image = url_for('static', filename='item_images/' + item.image)

    if form.validate_on_submit():
        if form.image.data:
            delete_image(item.image)
            picture_file = save_image(form.image.data)
            item.image = picture_file

        item.name = form.name.data
        item.manufacturer = form.manufacturer.data
        item.quantity = form.quantity.data
        item.summary = form.summary.data
        db.session.commit()
        flash('Item information has been updated!', 'success')
        return redirect(url_for('routes.view_item', item_id=item.id))

    elif request.method == 'GET':
        form.name.data = item.name
        form.manufacturer.data = item.manufacturer
        form.quantity.data = item.quantity
        form.summary.data = item.summary

    return render_template('item_form.html', form=form, legend='Update Item Form', image=image)


@routes.route('/delete/<int:item_id>', methods=['GET'])
def delete_item(item_id):
    item = Items.query.get_or_404(item_id)  # Get post with this id or get 404 meaning page does not exist
    db.session.delete(item)
    db.session.commit()
    flash('Item has been deleted!', 'danger')
    return redirect(url_for('routes.home'))
