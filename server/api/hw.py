from flask import Blueprint, request

from database import db

from config import Config

hw_blueprint = Blueprint('hw', __name__)

@hw_blueprint.route('/hw', methods=['GET'])
def handle_hw():
  if request.method == 'GET':
    if Config.CONTAINER_NAME != None:
      return {
        'hello': 'world',
        'serverContainerName': Config.CONTAINER_NAME
      }
    elif Config.POD_NAME != None:
      return {
        'hello': 'world',
        'serverPodName': Config.POD_NAME
      }
    else:
      return {'hello': 'world'}