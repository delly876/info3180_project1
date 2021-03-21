from . import db


class Property(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True)
    norooms = db.Column(db.Integer)
    nobath = db.Column(db.Integer)
    location = db.Column(db.String(255))
    price = db.Column(db.Float)
    type = db.Column(db.String(255))
    description = db.Column(db.String(255))
    filename = db.Column(db.String(255))

    def __init__(self, name, norooms, nobath, location, price, type, description, filename):
        self.name = name
        self.norooms = norooms
        self.nobath = nobath
        self.location = location
        self.price = price
        self.type = type
        self.description = description
        self.filename = filename

    def __repr__(self):
        return '%r%r%r' % (self.name, self.location, self.price)
        