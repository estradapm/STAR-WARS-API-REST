"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Character, Planet, Vehicle, UserFavoriteCharacter, UserFavoritePlanets
from api.utils import generate_sitemap, APIException
from flask_cors import CORS

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)

#USER

@api.route('/get_user', methods=['GET'])
def get_user():
    users = User.query.all()
    results = []
    for user in users:
       results.append(user.serialize())
    response_body = {
        'message': 'Ok',
        'results':results
    }

    return jsonify(response_body), 200


@api.route('/post_user', methods=['POST'])
def post_user():
    request_body = request.get_json()
    user =  User(email = request_body['email'],
                 password = request_body['password'],
                 is_active = request_body['is_active'])
    db.session.add(user)
    db.session.commit()

    return jsonify(request_body), 200


@api.route('/edit_user/<int:id>', methods=['PUT'])
def edit_user(id):
    request_body = request.get_json()
    user = User.query.get(id)
    if user is None:
        raise APIException('User not found', status_code=404)
    if "email" in request_body:
        user.email = request_body["email"]
    if "password" in request_body:
        user.password = request_body ["password"]
    if "is_active" in request_body:
        user.is_active = request_body ["is_active"]

    db.session.commit()
    return jsonify(user.serialize()), 200

@api.route('/delete_user/<int:id>', methods=['DELETE'])
def delete_user (id):
    user = User.query.get(id)
    if user is None:
        raise APIException('User not found', status_code=404)
    db.session.delete(user)
    db.session.commit()
    return jsonify("Ok"), 200



#CHARACTER
@api.route('/get_character', methods=['GET'])
def get_character():
    characters = Character.query.all()
    results = []
    for character in characters:
        results.append(character.serialize())
    response_body = {
        'message': 'Ok',
        'results': results
    }

    return jsonify(response_body), 200


@api.route('/get_character_id/<int:id>', methods=['GET'])
def get_character_id(id):
    character = Character.query.get(id)
    
    if character is None:
        response_body = {
            'message': 'Character not found',
            'results': []
        }
        return jsonify(response_body), 
    
    result = character.serialize()  
    
    response_body = {
        'message': 'Ok',
        'results': result
    }

    return jsonify(response_body), 200


@api.route('/delete_character/<int:id>', methods=['DELETE'])
def delete_character (id):
    character = Character.query.get(id)
    if character is None:
        raise APIException('Character not found', status_code=404)
    db.session.delete(character)
    db.session.commit()
    return jsonify("Ok"), 200


@api.route('/edit_character/<int:id>', methods=['PUT'])
def edit_character(id):
    request_body = request.get_json()
    character = Character.query.get(id)
    if character is None:
        raise APIException('Character not found', status_code=404)
    if "name" in request_body:
        character.name = request_body["name"]
    if "description" in request_body:
        character.description = request_body ["description"]

    db.session.commit()
    return jsonify(character.serialize()), 200

@api.route('/post_character', methods=['POST'])
def post_character():
    request_body = request.get_json()
    character =  Character(name = request_body['name'],
                 description = request_body['description'])
    db.session.add(character)
    db.session.commit()

    return jsonify(request_body), 200


#PLANET

@api.route('/get_planet', methods=['GET'])
def get_planet():
    planets = Planet.query.all()
    results = []
    for planet in planets:
        results.append(planet.serialize())
    response_body = {
        'message': 'Ok',
        'results': results
    }

    return jsonify(response_body), 200

@api.route('/get_planet_id/<int:id>', methods=['GET'])
def get_planet_id(id):
    planet = Planet.query.get(id)
    
    if planet is None:
        response_body = {
            'message': 'Planet not found',
            'results': []
        }
        return jsonify(response_body), 
    
    result = planet.serialize()  
    
    response_body = {
        'message': 'Ok',
        'results': result
    }

    return jsonify(response_body), 200

@api.route('/delete_planet/<int:id>', methods=['DELETE'])
def delete_planet (id):
    planet = Planet.query.get(id)
    if planet is None:
        raise APIException('Planet not found', status_code=404)
    db.session.delete(planet)
    db.session.commit()
    return jsonify("Ok"), 200


@api.route('/edit_planet/<int:id>', methods=['PUT'])
def edit_planet(id):
    request_body = request.get_json()
    planet = Planet.query.get(id)
    if planet is None:
        raise APIException('Planet not found', status_code=404)
    if "name" in request_body:
        planet.name = request_body["name"]
    if "temperature" in request_body:
        planet.temperature = request_body ["temperature"]
    if "image_url" in request_body:
        planet.image_url = request_body ["image_url"]

    db.session.commit()
    return jsonify(planet.serialize()), 200

@api.route('/post_planet', methods=['POST'])
def post_planet():
    request_body = request.get_json()
    planet =  Planet(name = request_body['name'],
                 temperature = request_body['temperature'])
    db.session.add(planet)
    db.session.commit()

    return jsonify(request_body), 200


#VEHICLE

@api.route('/get_vehicle', methods=['GET'])
def get_vehicle():
    vehicles = Vehicle.query.all()
    results = []
    for vehicle in vehicles:
        results.append(vehicle.serialize())
    response_body = {
        'message': 'Ok',
        'results': results
    }

    return jsonify(response_body), 200


@api.route('/get_vehicle_id/<int:id>', methods=['GET'])
def get_vehicle_id(id):
    vehicle = Vehicle.query.get(id)
    
    if vehicle is None:
        response_body = {
            'message': 'Vehicle not found',
            'results': []
        }
        return jsonify(response_body), 
    
    result = vehicle.serialize()  
    
    response_body = {
        'message': 'Ok',
        'results': result
    }

    return jsonify(response_body), 200

@api.route('/delete_vehicle/<int:id>', methods=['DELETE'])
def delete_vehicle (id):
    vehicle = Vehicle.query.get(id)
    if vehicle is None:
        raise APIException('Vehicle not found', status_code=404)
    db.session.delete(vehicle)
    db.session.commit()
    return jsonify("Ok"), 200


@api.route('/edit_vehicle/<int:id>', methods=['PUT'])
def edit_vehicle(id):
    request_body = request.get_json()
    vehicle = Vehicle.query.get(id)
    if vehicle is None:
        raise APIException('Vehicle not found', status_code=404)
    if "name" in request_body:
        vehicle.name = request_body["name"]
    if "price" in request_body:
        vehicle.price = request_body ["price"]
    if "image_url" in request_body:
        vehicle.image_url = request_body ["image_url"]

    db.session.commit()
    return jsonify(vehicle.serialize()), 200

@api.route('/post_vehicle', methods=['POST'])
def post_vehicle():
    request_body = request.get_json()
    vehicle =  Vehicle(name = request_body['name'],
                 price = request_body['price'])
    db.session.add(vehicle)
    db.session.commit()

    return jsonify(request_body), 200


#USER FAVORITE PLANETS

@api.route('/user/favorite_planets/<int:user_id>', methods=['GET'])
def get_favorite_planet(user_id):
       favorites = UserFavoritePlanets.query.filter(UserFavoritePlanets.user_id == user_id).all()
       results = [favorite.serialize() for favorite in favorites]
       response_body = {'message': 'Ok',
                        'results':results}
       
       return jsonify(response_body), 200

@api.route('/favorite_planets/<int:user_id>', methods=['POST'])
def post_favorite_planet (user_id):
    request_body = request.get_json()
    favorite = UserFavoritePlanets(
        user_id = user_id,
        favorite_planet_id = request_body['favorite_planet_id']
    )
    db.session.add(favorite)
    db.session.commit()
    return jsonify(request_body), 200

@api.route("/user/favorite_planets/<int:favorite_planet_id>", methods=["DELETE"])
def delete_favorite_planet(favorite_planet_id):
    favorite = UserFavoritePlanets.query.get(favorite_planet_id)
    if favorite is None:
        return jsonify({"error": "Favorite not found"}), 404

    db.session.delete(favorite)
    db.session.commit()
    
    return jsonify({"message": "Favorite deleted successfully"}), 200

#USER FAVORITE CHARACTER

@api.route('/user/favorite_character/<int:user_id>', methods=['GET'])
def get_favorite_character(user_id):
       favorites = UserFavoriteCharacter.query.filter(UserFavoriteCharacter.user_id == user_id).all()
       results = [favorite.serialize() for favorite in favorites]
       response_body = {'message': 'Ok',
                        'results':results}
       
       return jsonify(response_body), 200

@api.route('/favorite_character/<int:user_id>', methods=['POST'])
def post_favorite_character (user_id):
    request_body = request.get_json()
    favorite = UserFavoriteCharacter(
        user_id = user_id,
        favorite_planet_id = request_body['favorite_planet_id']
    )
    db.session.add(favorite)
    db.session.commit()
    return jsonify(request_body), 200

@api.route("/user/favorite_character/<int:favorite_character_id>", methods=["DELETE"])
def delete_favorite_character(favorite_character_id):
    favorite = UserFavoriteCharacter.query.get(favorite_character_id)
    if favorite is None:
        return jsonify({"error": "Favorite not found"}), 404

    db.session.delete(favorite)
    db.session.commit()
    
    return jsonify({"message": "Favorite deleted successfully"}), 200
