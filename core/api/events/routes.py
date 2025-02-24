from flask import Blueprint, jsonify


# Blueprint configuration
events = Blueprint('events', __name__)


@events.route('/events', methods=['GET'])
def get_events():
    return jsonify({'data': 'There\'s events!'})
