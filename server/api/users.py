from flask import Blueprint, request

from database import db
from models.user import User

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/users', methods=['GET', 'POST'])
def handle_users():
  if request.method == 'GET':
    users = [user.to_json() for user in User.query.all()]
    return {'count': len(users), 'users': users}

  elif request.method == 'POST':
    if request.is_json:
      new_user = User.from_json(request.get_json())
      db.session.add(new_user)
      db.session.commit()
      return {'message': f'User {new_user.id} ({new_user.first_name} {new_user.last_name}, {new_user.email}) was successfully created.'}
    else:
      return {'error': 'The request payload must be in JSON format.'}

@users_blueprint.route('/user/<int:user_id>', methods=['GET', 'PATCH', 'DELETE'])
def handle_user_by_id(user_id):
  user = User.query.get_or_404(user_id)

  if request.method == 'GET':
    return user.to_json()
  
  elif request.method == 'PATCH':
    updated_fields = user.update_fields(request.json)
    db.session.commit()
    return { 'updatedFields': updated_fields }

  elif request.method == 'DELETE':
    db.session.delete(user)
    db.session.commit()
    return { 'message': f'User {user_id} was successfully deleted' }