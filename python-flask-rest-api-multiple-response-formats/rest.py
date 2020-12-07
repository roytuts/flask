from flask import request
from flask_restful import Resource

class Greet(Resource):

	def get(self):
		return {'message' : 'Hello, how are you?'}
	
	def post(self):
		req = request.get_json()
		print('req', req)
		return req, 201

class GreetName(Resource):
	def get(self, name):
		return {'message' : 'Hello ' + name + ', how are you?'}