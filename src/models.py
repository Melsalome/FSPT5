from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "username": self.username,
            "email": self.email
        }
    
class Planet(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    diameter = db.Column(db.Integer)
    population = db.Column(db.BigInteger)

    def __repr__(self):
        return '{}'.format(self.name)
    
    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "population": self.population
        }
    
class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    height = db.Column(db.Float)
    eye_color = db.Column(db.String(250))

    def __repr__(self):
        return '{}'.format(self.name)

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "weight": self.weight
        }

class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(250), nullable=False)
    length = db.Column(db.Float)
    crew = db.Column(db.Integer)
    vehicle_class = db.Column(db.String(250))

    def __repr__(self):
        return '{}'.format(self.name)

    def serialize(self):
        return{
            "id": self.id,
            "model": self.model,
            "lenght": self.lenght,
            "crew": self.crew,
            "vehicle_class": self.vehicle_class
        }
    
class Favorite(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_character = db.Column(db.Integer, db.ForeignKey('characters.id'))
    user_planet = db.Column(db.Integer, db.ForeignKey('planets.id'))
    user = db.relationship(User)
    character = db.relationship(Character)
    planet = db.relationship(Planet)

    def __repr__(self):
        return '{}'.format(self.id)

    def serialize(self):
        return{
            "id": self.id,
            "user_id": self.user_id,
            "user_character": self.user_character,
            "user_planet": self.user_planet
        }
    