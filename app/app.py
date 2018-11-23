from flask import Flask
from flask_restful import Api
from config import Config, ProductionConfig
from resources import UserResource, FeatureRequestResource
from db import db

app = Flask(__name__)
app.config.from_object(Config)
db.app = app
db.init_app(app)

api = Api(app)

api.add_resource(UserResource, '/user')
api.add_resource(FeatureRequestResource, '/feature')

if __name__ == '__main__':
    app.run(debug=True)