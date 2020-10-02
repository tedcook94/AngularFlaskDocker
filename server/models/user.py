from sqlalchemy import func
from sqlalchemy.dialects.postgresql import INTEGER, VARCHAR, BOOLEAN, TIMESTAMP

from database import db
from models.base_model import BaseModel

class User(BaseModel, db.Model):
  __tablename__ = 'users'

  id = db.Column(INTEGER, primary_key=True, autoincrement=True)
  first_name = db.Column(VARCHAR(128), nullable=False)
  last_name = db.Column(VARCHAR(128), nullable=False)
  email = db.Column(VARCHAR(128), nullable=False, unique=True)
  password = db.Column(VARCHAR(128), nullable=False)
  active = db.Column(BOOLEAN, default=True, nullable=False)
  created_date = db.Column(TIMESTAMP, default=func.now(), nullable=False)

  def __init__(self, first_name, last_name, email, password, active=True):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.password = password
    self.active = active

  def __repr__(self):
    return f"<User {self.id} ({self.first_name} {self.last_name}, {self.email}) {'is active' if self.active else 'is not active'}>"

  # Create a JSON object from a User
  def to_json(self):
    return {
      'id': self.id,
      'name': {
        'first': self.first_name,
        'last': self.last_name
      },
      'email': self.email,
      'password': self.password,
      'active': self.active,
      'created': self.created_date
    }
  
  # Create a User from a JSON object
  def from_json(data: dict):
    return User(
      first_name=data['firstName'], 
      last_name=data['lastName'], 
      email=data['email'],
      password=data['password'],
      active=data.get('active', True)
    )

  # Update User's fields based on fields in JSON object
  def update_fields(self, data: dict):
    updated_fields: list = []
    if 'firstName' in data:
      self.first_name = data['firstName']
      updated_fields.append('firstName')
    if 'lastName' in data:
      self.last_name = data['lastName']
      updated_fields.append('lastName')
    if 'email' in data:
      self.email = data['email']
      updated_fields.append('email')
    if 'password' in data:
      self.password = data['password']
      updated_fields.append('password')
    if 'active' in data:
      self.active = data['active']
      updated_fields.append('active')
    
    return updated_fields