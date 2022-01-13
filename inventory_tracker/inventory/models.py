from inventory_tracker import db


class Items(db.Model):
    id = db.Column(db.Integer,
                   primary_key=True)  # This is primary key aka unique id... this will be assigned automatically since it is unique
    quantity = db.Column(db.Integer, nullable=False)  # This is primary key aka unique id
    name = db.Column(db.String(20), nullable=False)  # max length is 20 and we need one so cant be null
    manufacturer = db.Column(db.String(40), nullable=False)  # max length is 40 and we need one so cant be null
    summary = db.Column(db.String(100), nullable=False)  # max length is 40 and we need one so cant be null
    category = db.Column(db.String(20), nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    retail_price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(500), nullable=True)
    image = db.Column(db.String(40), nullable=False, default='default.jpg')

    def __repr__(self):
        return f"Item('{self.manufacturer}', '{self.name}', '{self.quantity}','{self.summary}', " \
               f"'{self.category}', '{self.unit_price}', '{self.retail_price}','{self.description}', '{self.image}')"
