from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    is_active = db.Column(db.Boolean(), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_active": self.is_active
            # no serializar la contraseña por razones de seguridad
        }

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    birthday = db.Column(db.DateTime, nullable=False)
    image_url = db.Column(db.String(250))
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"), nullable=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicle.id"), nullable=True)

    def __repr__(self):
        return f'<Character {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "birthday": self.birthday.isoformat() if self.birthday else None,
            "image_url": self.image_url,
            "planet_id": self.planet_id,
            "vehicle_id": self.vehicle_id
        }

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    temperature = db.Column(db.Float)
    image_url = db.Column(db.String(250))

    def __repr__(self):
        return f'<Planet {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "temperature": self.temperature,
            "image_url": self.image_url,
        }

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float)
    image_url = db.Column(db.String(250))

    def __repr__(self):
        return f'<Vehicle {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "image_url": self.image_url,
        }

class Favourite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey("character.id"), nullable=True)
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"), nullable=True)

    def __repr__(self):
        return f'<Favourite {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id,
        }