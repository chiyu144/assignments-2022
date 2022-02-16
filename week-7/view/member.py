from flask import Blueprint, jsonify, render_template, redirect, url_for, request, session, g

blueprint_member = Blueprint('member', __name__)

@blueprint_member.route('/member/', methods=['GET', 'POST'])
def member():
  if request.method == 'GET':
    if 'user_id' in session:
      g.cursor.execute('SELECT name FROM member WHERE username = %s', (session.get('user_id'), ))
      user_name = g.cursor.fetchone()
      return render_template('member.html', header_title = f"{user_name[0]}您好，這是會員頁")
    return redirect(url_for('index.index'))
  if request.method == 'POST':
    user_name = request.get_json()['userName']
    if 'user_id' in session and user_name:
      g.cursor.execute('UPDATE member SET name = %s WHERE username = %s', (user_name, session.get('user_id')))
      g.db.commit()
      return jsonify({ 'ok': True })
    else:
      return jsonify({ 'error': True })