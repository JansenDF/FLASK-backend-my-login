from urllib import response
from flask import request, jsonify, json
from flask_restx import Resource
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

from ..util.dto import UserDto
from ..service.user_services import getAllUsers, createUser, get_user

api = UserDto.api
_user = UserDto.user


@api.route('/list')
class UserList(Resource):
    @api.doc('list_of_registered_user')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered users"""
        return getAllUsers()  # call the new service

@api.route('/create')
class UserCreate(Resource):
    @api.response(200, 'User sucessfully created.')
    @api.doc('Create a new Users')
    @api.expect(_user, validate=True)
    def post(self):
        """Create a new User"""
        data = request.json
        return createUser(data)  # call the new service

# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@api.route('/token', methods=['POST'])
class UserToken(Resource):
    def post(self):
        data = request.json

        user = get_user(data)
        userPasswordChecked = user['passwordChecked']

        if not userPasswordChecked:
            response_object = {
                "msg": "Bad username or password"
            }
            return response_object, 401

        access_token = create_access_token(identity=data['email'])
        return jsonify(token=access_token, user=user)