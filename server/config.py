import os

# Fetches environment variables that have been passed in from Docker
class Config(object):
  DB_USER = os.getenv('DB_USER')
  DB_PASSWORD = os.getenv('DB_PASSWORD')
  DB_HOSTNAME = os.getenv('DB_HOSTNAME')
  DB_NAME = os.getenv('DB_NAME')
  SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:5432/{3}'.format(DB_USER, DB_PASSWORD, DB_HOSTNAME, DB_NAME)
  SQLALCHEMY_TRACK_MODIFICATIONS = False

  DEVELOPMENT = os.getenv('FLASK_DEVELOPMENT')
  DEBUG = os.getenv('FLASK_DEBUG')

  CONTAINER_NAME = os.getenv('CONTAINER_NAME')
  POD_NAME = os.getenv('POD_NAME')