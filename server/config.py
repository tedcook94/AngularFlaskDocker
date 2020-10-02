import os

# Fetches environment variables that have been passed in from Docker
class Config(object):
  DB_USER = os.getenv('DB_USER')
  DB_PASSWORD = os.getenv('DB_PASSWORD')
  DB_NAME = os.getenv('DB_NAME')
  SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@database:5432/{2}'.format(DB_USER, DB_PASSWORD, DB_NAME)
  SQLALCHEMY_TRACK_MODIFICATIONS = False

  DEVELOPMENT = os.getenv('FLASK_DEVELOPMENT')
  DEBUG = os.getenv('FLASK_DEBUG')