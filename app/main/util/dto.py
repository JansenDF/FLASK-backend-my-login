
from flask_restx import Namespace, fields


class LogDto:
    api = Namespace('log', description='log related operations')
    log = api.model('log', {
        'responsible_code': fields.Integer(required=True, description='foreign key user id'),
        'table': fields.String(required=True, description='table type'),
        'operation_code': fields.Integer(required=True, description='code operation'),
        'description': fields.String(description='description')
    })

class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'name': fields.String(required=True, description='name'),
        'username': fields.String(required=True, description='username'),
        'email': fields.String(required=True, description='email'),
        'password_hash': fields.String(required=True, description='password')
    })

class LoginDto:
    api = Namespace('user', description='user related operations')
    login = api.model('user', {
                'id': fields.Integer(Required=True, description='id'),
                'name': fields.String(required=True, description='name'),
                'username': fields.String(required=True, description='username'),
                'email': fields.String(required=True, description='email')
            },
    )