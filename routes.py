from flask import Blueprint, render_template, flash, redirect, url_for
from forms import NewItemForm, UpdateItemForm

routes = Blueprint("routes", __name__)

inventory = [
    {'name': 'Iphone',
     'manufacturer': 'Apple',
     'quantity': '100',
     'summary': 'This is a high tech device'
     },
    {'name': 'Pizza',
     'manufacturer': 'PizzaHut',
     'quantity': '50',
     'summary': 'This is very yummy'
     }
]


@routes.route('/')
@routes.route('/home')
def home():
    return render_template('homepage.html', inventory=inventory)


@routes.route('/new-item', methods=['GET', 'POST'])
def new_item():
    form = NewItemForm()
    if form.validate_on_submit():
        flash(f'Item entry for {form.name.data} created!', 'success')
        return redirect(url_for('routes.home'))
    return render_template('newitem.html', form=form)


@routes.route('/update-item')
def update_item():
    form = UpdateItemForm()
    return render_template('update-item.html', form=form)
