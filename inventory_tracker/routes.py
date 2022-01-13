from flask import Blueprint, render_template
from inventory_tracker.inventory.models import Items

main = Blueprint("main", __name__)


@main.route('/')
@main.route('/home')
def home():
    inventory = Items.query.all()
    return render_template('homepage.html', inventory=inventory)









