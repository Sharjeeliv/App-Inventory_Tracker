from flask import render_template, flash, redirect, url_for, request, Blueprint
from inventory_tracker.inventory.forms import ItemForm
from inventory_tracker import db
from inventory_tracker.inventory.models import Items
from inventory_tracker.inventory.utils import delete_image, save_image

inventory = Blueprint("inventory", __name__)


@inventory.route('/new', methods=['GET', 'POST'])
def new_item():
    form = ItemForm()

    # Add an entry to the database if the form data is valid (passes through the WTForms validators)
    if form.validate_on_submit():
        item = Items(name=form.name.data, manufacturer=form.manufacturer.data, quantity=form.quantity.data,
                     summary=form.summary.data, category=form.category.data, unit_price=form.unit_price.data,
                     retail_price=form.retail_price.data, description=form.description.data)

        # Manipulate and store the new uploaded image
        if form.image.data:
            picture_file = save_image(form.image.data)
            image = picture_file
            item.image = image

        db.session.add(item)
        db.session.commit()
        flash(f'Item entry for {form.name.data} created!', 'success')
        return redirect(url_for('main.home'))

    return render_template('item_form.html', form=form, legend='New Item Form',
                           image=url_for('static', filename='item_images/default.jpg'))


@inventory.route('/item/<int:item_id>', methods=['GET', 'POST'])
def view_item(item_id):
    item = Items.query.get_or_404(item_id)
    image = url_for('static', filename='item_images/' + item.image)
    return render_template('item_view.html', item=item, legend='Update Item Form', image=image)


@inventory.route('/update/<int:item_id>', methods=['GET', 'POST'])
def update_item(item_id):
    # Get item entry with this id (item_id) or get 404 meaning page does not exist
    item = Items.query.get_or_404(item_id)
    form = ItemForm()
    image = url_for('static', filename='item_images/' + item.image)

    if form.validate_on_submit():
        # If user uploads new image, delete the previous one and save the new one
        if form.image.data:
            delete_image(item.image)
            picture_file = save_image(form.image.data)
            item.image = picture_file

        # Update all database columns for a valid submitted entry
        item.name = form.name.data
        item.manufacturer = form.manufacturer.data
        item.quantity = form.quantity.data
        item.summary = form.summary.data
        item.category = form.category.data
        item.unit_price = form.unit_price.data
        item.retail_price = form.retail_price.data
        item.description = form.description.data

        db.session.commit()
        flash('Item information has been updated!', 'success')
        return redirect(url_for('inventory.view_item', item_id=item.id))

    # When the user 'gets' the page, autofill the form with data from the corresponding item
    # entry in the database
    elif request.method == 'GET':
        form.name.data = item.name
        form.manufacturer.data = item.manufacturer
        form.quantity.data = item.quantity
        form.summary.data = item.summary
        form.category.data = item.category
        form.unit_price.data = item.unit_price
        form.retail_price.data = item.retail_price
        form.description.data = item.description

    return render_template('item_form.html', form=form, legend='Update Item Form', image=image)


@inventory.route('/delete/<int:item_id>', methods=['GET'])
def delete_item(item_id):
    item = Items.query.get_or_404(item_id)  # Get post with this id or get 404 meaning page does not exist
    delete_image(item.image)
    db.session.delete(item)
    db.session.commit()
    flash('Item has been deleted!', 'danger')
    return redirect(url_for('main.home'))
