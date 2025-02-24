from flask import Blueprint


# Blueprint configuration
blueprint = Blueprint('events', __name__)


@blueprint.route('/hello', methods=['GET'])
def hello_world():
    return 'Hello, World!'
