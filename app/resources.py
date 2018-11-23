from flask_restful import Resource, abort, reqparse
from db import db

class UserResource(Resource):
	def post(self):
		''' LOGIN - ASSUME USER ALREADY HAS AN ACCOUNT '''
		pass


class FeatureRequestResource(Resource):
	def post(self):
		''' CREATE A NEW FEATURE REQUEST '''
		pass

	def get(self, id = None):
		''' GET A LIST OF FEATURE REQUESTS OF JUST ONE FEATURE REQUEST '''
		pass

	def put(self, id):
		''' UPDATE FEATURE REQUEST '''
		pass

	def delete(self, id):
		''' DELETE FEATURE REQUEST '''
		pass