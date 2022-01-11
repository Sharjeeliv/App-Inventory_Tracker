from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # Created app
app.config['SECRET_KEY'] = '6ba12202b0c980a1c3d10b3c03482569'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from routes import routes

app.register_blueprint(routes)

if __name__ == '__main__':
    app.run()
