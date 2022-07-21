import jwt
from app.main.model.user import User 
from app.main import db
from flask import jsonify

def getAllUsers():
    users = User.query.all()
    return users

def user_add(newUser):
    db.session.add(newUser)
    db.session.commit()

def createUser(data):
    newUser = User(
        name = data['name'],
        username = data['username'],
        email = data['email']
    )
    newUser.set_password(data['password_hash'])
    user_add(newUser)

    response_object = {
        'status': 'Success',
        'message': 'User successfully created'
    }
    return response_object, 200

def get_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        response_object = {
            'status': 'Failed',
            'message': 'User or Password invalid!'
        }
        return response_object, 401

    password = data['password']
    password_checked = user.check_password(password)
    if password_checked:
        userLogged = {
            "name": user.name,
            "email": user.email,
            "password_hash": user.password_hash,
            "passwordChecked": password_checked
        }
        return userLogged
    else:
        userLogged = {
            "passwordChecked": False
        }
        return userLogged
