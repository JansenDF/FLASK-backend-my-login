import jwt
from .. import db
from ..config import Config
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app.main import login


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    username = db.Column(db.String(64))
    email = db.Column(db.String(64))
    password_hash = db.Column(db.String(64))

    def __repr__(self):
        return "<User '{}'>".format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # def generate_token(data):
    #     payload_data = {
    #         "sub": data['email'],
    #         "name": data['name'],
    #         "nickname": data['username']
    #     }
    #     token = jwt.encode(
    #         payload = payload_data,
    #         key = Config.SECRET_KEY
    #     )
    #     return token
    
    # def check_token(data):
    #     token = data['token']
    #     tokenDecode = jwt.decode(token, key=Config.SECRET_KEY, algorithms=['HS256', ])
    #     if data['token'] == tokenDecode:
    #         return token
    #     else:
    #         return

    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))