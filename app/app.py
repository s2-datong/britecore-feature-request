from flask import Flask, send_from_directory
from flask_restful import Api
from config import Config, ProductionConfig
from resources import UserResource, FeatureRequestResource, LookUpClientResource, LookUpPriorityResource, LookUpProductAreas
from db import db

app = Flask(__name__, static_folder='static', static_url_path='')
app.config.from_object(Config)
db.app = app
db.init_app(app)

# static index route
@app.route('/')
@app.route('/index')
def index():
    return send_from_directory('static', 'index.html')

api = Api(app)

api.add_resource(UserResource, '/user')
api.add_resource(FeatureRequestResource, '/feature', '/feature/<id>', endpoint='feature')
api.add_resource(LookUpClientResource, '/clients')
api.add_resource(LookUpPriorityResource, '/priority/<string:client>')
api.add_resource(LookUpProductAreas, '/product_areas')

if __name__ == '__main__':
    app.run(debug=True)
    
    ''' 
    	Allow Remote connections and listen on port 80. Need to run with sudo 
    	app.run(host='0.0.0.0', port=80)
    '''
