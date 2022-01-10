from app import db


class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # This is primary key aka unique id... this will be assigned automatically since it is unique
    quantity = db.Column(db.Integer, nullable=False)  # This is primary key aka unique id
    name = db.Column(db.String(20), nullable=False)  # max length is 20 and we need one so cant be null
    manufacturer = db.Column(db.String(40), nullable=False)  # max length is 40 and we need one so cant be null
    summary = db.Column(db.String(500), nullable=False)  # max length is 40 and we need one so cant be null
    image = db.Column(db.String(40), nullable=False, default='default.jpg')

    def __repr__(self):
        return f"Item('{self.manufacturer}', '{self.name}', '{self.quantity}','{self.summary}', '{self.image}')"
