from flask import request
from flask_restx import Resource

from ..util.dto import LogDto

api = LogDto.api
_log = LogDto.log


@api.route('/')
class LogList(Resource):
    @api.doc('list_of_registered_log')
    @api.marshal_list_with(_log, envelope='data')
    def get(self):
        """List all registered logs"""
        return ""  # call the new service

    @api.response(201, 'Log sucessfully created.')
    @api.doc('Create a new Log')
    @api.expect(_log, validate=True)
    def post(self):
        """Create a new Log"""
        data = request.json
        return ""  # call the new service
