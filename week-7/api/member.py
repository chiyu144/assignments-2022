from flask import Blueprint, jsonify, request, session, current_app

blueprint_member_api = Blueprint('member_api', __name__)

@blueprint_member_api.route('/member', methods=['POST'])
def memberApi():
  if request.method == 'POST':
    user_name = request.get_json()['userName']
    if 'user_id' in session and user_name:
      cnx = current_app.db_cnx()
      cursor = cnx.cursor()
      cursor.execute('UPDATE member SET name = %s WHERE username = %s', (user_name, session.get('user_id')))
      cnx.commit()
      cursor.close()
      cnx.close()
      return jsonify({ 'ok': True })
    else:
      return jsonify({ 'error': True })