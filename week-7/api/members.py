from flask import Blueprint, request, jsonify
from decorators import with_cnx

blueprint_members_api = Blueprint('members_api', __name__)

@with_cnx(need_commit = False)
def queryMemberData(cursor, user_id):
  cursor.execute('SELECT id, name, username FROM member WHERE username = %s', (user_id, ))
  user = cursor.fetchone()
  return user

@blueprint_members_api.route('/members', methods=['GET'])
def membersApi():
  result = None
  if request.method == 'GET':
    user_id = request.args.get('username')
    # cnx = current_app.db_cnx()
    # cursor = cnx.cursor()
    # cursor.execute('SELECT id, name, username FROM member WHERE username = %s', (user_id, ))
    # user = cursor.fetchone()
    member_data = queryMemberData(user_id)
    if member_data:
      result = {
        'id': member_data[0],
        'name': member_data[1],
        'username': member_data[2],
      }
    # cursor.close()
    # cnx.close()
  return jsonify({'data': result})