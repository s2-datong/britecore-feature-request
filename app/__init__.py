from flask import Flask
from flask_restful import Api
from config import Config, ProductionConfig
from flask_sqlalchemy import SQLAlchemy
import resources

app = Flask(__name__)
app.config.from_object(Config)

api = Api(app)
db = SQLAlchemy(app)

api.add_resource(UserResource, '/user')
api.add_resource(FeatureRequestResource, '/feature')

if __name__ == '__main__':
    app.run(debug=True)