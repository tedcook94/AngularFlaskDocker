import math
from flask import Blueprint, request

from database import db

from config import Config

cpu_blueprint = Blueprint('cpu', __name__)

@cpu_blueprint.route('/cpu', methods=['GET'])
def handle_cpu():
  if request.method == 'GET':
    x = 0.0001
    for i in range(1000000):
      x += math.sqrt(x)
    return {'x': x}