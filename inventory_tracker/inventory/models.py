from inventory_tracker import db


class Items(db.Model):
    """
    SQLAlchmey is an object relational mapper (ORM) that allows easy usage and implementation of an SQL
    database. It allows the SQL database to be represented as an object with columns represented as variables.
    Flask and WTForms are used to easily incorporate the database into the program.

    The database used is SQLITE since it is part of the python standard library, is lightweight and performant
    and easy to implement for the purposes of this project. However, by using a high level ORM this database can be
    substituted for another without much hassle.
    """

    # The id is the primary key (a unique id for internal usage). This value will be assigned automatically
    id = db.Column(db.Integer, primary_key=True)

    # Special requirements are listed such as if the column can be left empty (nullable), and the maximum length
    quantity = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(20), nullable=False)
    manufacturer = db.Column(db.String(40), nullable=False)
    summary = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(20), nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    retail_price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(500), nullable=True)
    image = db.Column(db.String(40), nullable=False, default='default.jpg')
    
    def __repr__(self):
        return f"Item('{self.manufacturer}', '{self.name}', '{self.quantity}','{self.summary}', " \
               f"'{self.category}', '{self.unit_price}', '{self.retail_price}','{self.description}', '{self.image}')"
