from flask import Flask, url_for
from routes import routes
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # Created app
app.register_blueprint(routes)
app.config['SECRET_KEY'] = '6ba12202b0c980a1c3d10b3c03482569'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'

db = SQLAlchemy(app)


class Items(db.Model):
    id = db.column(db.Integer, primary_key=True)  # This is primary key aka unique id
    quantity = db.column(db.Integer, nullable=False)  # This is primary key aka unique id
    name = db.column(db.String(20), nullable=False)  # max length is 20 and we need one so cant be null
    manufacturer = db.column(db.String(40), nullable=False)  # max length is 40 and we need one so cant be null
    summary = db.column(db.String(500), nullable=False)  # max length is 40 and we need one so cant be null
    image_file = db.column(db.String(40), nullable=False, default='default.jpg')

    def __repr__(self):
        return f"Item('{self.manufacturer}', '{self.name}', '{self.quantity}', '{self.image_file}')"


if __name__ == '__main__':
    app.run()
