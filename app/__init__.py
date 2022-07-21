from flask_restx import Api
from flask import Blueprint

from .main.controller.log_controller import api as log_ns
from .main.controller.user_controller import api as user_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTX API BOILER-PLATE WITH JWT',
          version='0.0.1',
          description='a boilerplate for flask restx web service'
          )

api.add_namespace(log_ns, path='/log')
api.add_namespace(user_ns, path='/user')