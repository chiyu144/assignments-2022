from flask import Blueprint, request, jsonify, g

blueprint_members_api = Blueprint('members_api', __name__)

@blueprint_members_api.route('/members', methods=['GET'])
def membersApi():
  user_data = None
  if request.method == 'GET':
    user_id = request.args.get('username')
    g.cursor.execute('SELECT id, name, username FROM member WHERE username = %s', (user_id, ))
    user = g.cursor.fetchone()
    if user:
      user_data = {
        'id': user[0],
        'name': user[1],
        'username': user[2],
      }
  return jsonify({'data': user_data})