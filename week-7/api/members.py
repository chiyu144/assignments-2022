from flask import Blueprint, request, jsonify, current_app

blueprint_members_api = Blueprint('members_api', __name__)

@blueprint_members_api.route('/members', methods=['GET'])
def membersApi():
  user_data = None
  if request.method == 'GET':
    user_id = request.args.get('username')
    cnx = current_app.db_cnx()
    cursor = cnx.cursor()
    cursor.execute('SELECT id, name, username FROM member WHERE username = %s', (user_id, ))
    user = cursor.fetchone()
    if user:
      user_data = {
        'id': user[0],
        'name': user[1],
        'username': user[2],
      }
    cursor.close()
    cnx.close()
  return jsonify({'data': user_data})