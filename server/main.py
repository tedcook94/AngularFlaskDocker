from flask import Flask
import os

from database import db
from config import Config

# App initialization
app = Flask(__name__)
app.config.from_object(Config())
app.url_map.strict_slashes = False
db.init_app(app)

# Register blueprints
from api.hw import hw_blueprint
from api.users import users_blueprint

app.register_blueprint(hw_blueprint, url_prefix='/api')
app.register_blueprint(users_blueprint, url_prefix='/api')


if __name__ == '__main__':
  app.run(host='0.0.0.0')