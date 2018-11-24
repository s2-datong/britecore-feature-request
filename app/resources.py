import uuid
from flask_restful import Resource, reqparse, inputs
from datetime import datetime
from models import User, FeatureRequest, db

class UserResource(Resource):
	def post(self):
		''' LOGIN - ASSUME USER ALREADY HAS AN ACCOUNT '''
		parser = reqparse.RequestParser(trim = True, bundle_errors = True)
		parser.add_argument('username', type=str, required=True, help='Error Username is required')
		parser.add_argument('password', type=str, required=True, help='Error Password is required')
		data = parser.parse_args()
		user = User.query.filter_by(username=data['username'], password=data['password']).first()
		if user is None:
			return {"status": 401, "message": "Invalid Username/Password Supplied"}

		user.session_token = str(uuid.uuid4())
		db.session.commit()

		return {"status": 200, "message": "login successful", "token": user.session_token}
		


class FeatureRequestResource(Resource):
	def post(self):
		''' CREATE A NEW FEATURE REQUEST '''

		parser = reqparse.RequestParser( trim = True, bundle_errors = True )
		parser.add_argument('title', type=str, required=True, help='Error Provide a title')
		parser.add_argument('description', type=str, required=True, help='Error Provide a description')
		parser.add_argument('client', type=str, required=True, help='Error Select a client')
		parser.add_argument('priority', type=int, required=True, help='Error select priority')
		parser.add_argument('date', type=inputs.date, required=True, help='Error Provide a target date')
		parser.add_argument('area', type=str, required=True, help='Error select a product area')
		parser.add_argument('token', type=str, required=True, location='headers', help='Authorization Required')
		data = parser.parse_args()

		feature = FeatureRequest(
				title = data['title'],
				description = data['description'],
				client = data['client'],
				priority = data['priority'],
				target_date = data['date'],
				product_area = data['area']
			)
		db.session.add(feature)
		db.session.commit()

		return {"status": 200, "message": "Feature request saved successfully"}

	def get(self, id = None):
		''' GET A LIST OF FEATURE REQUESTS OF JUST ONE FEATURE REQUEST '''
		parser = reqparse.RequestParser( trim = True, bundle_errors = True )
		parser.add_argument('token', type=str, required=True, location='headers', help='Authorization Required')
		data = parser.parse_args()

		if id is not None:
			request = FeatureRequest.query.get(id)
			feature = {
				"id": request.id,
				"title" : request.title,
				"description" : request.description,
				"client" : request.client,
				"priority" : request.priority,
				"target_date" : request.target_date.__str__(),
				"product_area" : request.product_area
			}
			return feature

		requests = FeatureRequest.query.all()
		result = []
		for request in requests:
			feature = {
				"id": request.id,
				"title" : request.title,
				"description" : request.description,
				"client" : request.client,
				"priority" : request.priority,
				"target_date" : request.target_date.__str__(),
				"product_area" : request.product_area
			}
			result.append(feature)
		return result

	def put(self, id):
		''' UPDATE FEATURE REQUEST '''
		parser = reqparse.RequestParser( trim = True, bundle_errors = True )
		parser.add_argument('title', type=str)
		parser.add_argument('description', type=str)
		parser.add_argument('client', type=str)
		parser.add_argument('priority', type=int)
		parser.add_argument('date', type=inputs.date)
		parser.add_argument('area', type=str)
		parser.add_argument('token', type=str, required=True, location='headers', help='Authorization Required')
		data = parser.parse_args()

		request = FeatureRequest.query.get(id)
		if request is None:
			return {"status": 404, "message": "No Feature Request with that id found"}

		''' Selectively Update request based on valid fields passed in'''
		if data['title'] is not None:
			request.title = data['title']

		if data['description'] is not None:
			request.description = data['description']

		if data['client'] is not None:
			request.client = data['client']

		if data['priority'] is not None:
			request.priority = data['priority']

		if data['date'] is not None:
			request.date = data['date']

		if data['area'] is not None:
			request.area = data['area']

		db.session.commit()

		return {"status": 200, "message": "Feature Request Has been Successfully updated"}

	def delete(self, id):
		''' DELETE FEATURE REQUEST '''
		parser = reqparse.RequestParser( trim = True, bundle_errors = True )
		parser.add_argument('token', type=str, required=True, location='headers', help='Authorization Required')
		data = parser.parse_args()

		request = FeatureRequest.query.get(id)
		if request is None:
			return {"status": 200, "message": "Feature Request Already Deleted"}

		db.session.delete(request)
		db.session.commit()

		return {"status": 200, "message": "Feature Request Successfully Deleted"}

class LookUpClientResource(Resource):
	def get(self):
		return ['Client1', 'Client2', 'Client3']

class LookUpPriorityResource(Resource):
	def get(self, client):
		''' get priority numbers based on what client has selected '''
		
		''' Get All client requests'''
		ids = []
		requests = FeatureRequest.query.filter_by(client = client ).all()
		if len(requests) is 0:
			return [1, 2, 3, 4, 5]

		for request in requests:
			ids.append(request.priority)

		returnIds = []
		index = 1
		'''Build a priority selection of 5 digits apart from already chosen priority'''
		while len(returnIds) < 5:
			if index not in ids:
				returnIds.append(index)

			index += 1

		return returnIds

class LookUpProductAreas(Resource):
	def get(self):
		return [ 'Policies', 'Billing', 'Claims', 'Reports' ]