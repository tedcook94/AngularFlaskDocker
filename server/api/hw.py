from flask import Blueprint, request

from database import db

hw_blueprint = Blueprint('hw', __name__)

@hw_blueprint.route('/hw', methods=['GET'])
def handle_hw():
  if request.method == 'GET':
    return {'hello': 'world'}