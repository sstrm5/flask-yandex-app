# from flask import Blueprint
from flask_restx import Api, Resource
from api.events.routes import events as events_bp
from core import app

# Blueprint configuration
# api = Blueprint('api', __name__)
api = Api(app, title="API", doc='/api/docs')
main = api.namespace('/')


@main.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'message': 'Hello, World!'}


# api.register_blueprint(events_bp)
