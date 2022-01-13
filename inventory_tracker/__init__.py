from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from inventory_tracker.config import Config

db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)  # Created app
    app.config.from_object(config_class)

    db.init_app(app)

    # To avoid circular imports
    from inventory_tracker.inventory.routes import inventory
    from inventory_tracker.routes import main

    app.register_blueprint(main)
    app.register_blueprint(inventory)

    return app
