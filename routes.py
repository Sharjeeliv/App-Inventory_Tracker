from flask import Blueprint, render_template

routes = Blueprint("routes", __name__)


@routes.route('/')
@routes.route('/home')
def home():
    return render_template('main.html')


@routes.route('/new-item')
def item():
    return render_template('sidebar.html')