"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Character, Planet, Vehicle, Favourite
from api.utils import generate_sitemap, APIException
from flask_cors import CORS

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


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
