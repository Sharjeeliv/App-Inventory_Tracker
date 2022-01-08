from flask import Blueprint, render_template

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
    return render_template('main.html', inventory=inventory)


@routes.route('/new-item')
def item():
    return render_template('sidebar.html')
