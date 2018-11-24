from flask import Flask
from flask_restful import Api
from config import Config, ProductionConfig
from resources import UserResource, FeatureRequestResource, LookUpClientResource, LookUpPriorityResource
from db import db

app = Flask(__name__, static_folder='static', static_url_path='')
app.config.from_object(Config)
db.app = app
db.init_app(app)

api = Api(app)

api.add_resource(UserResource, '/user')
api.add_resource(FeatureRequestResource, '/feature', '/feature/<id>', endpoint='feature')
api.add_resource(LookUpClientResource, '/clients')
api.add_resource(LookUpPriorityResource, '/priority/<string:client>')

if __name__ == '__main__':
    app.run(debug=True)