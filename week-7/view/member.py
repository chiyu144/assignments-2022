from flask import Blueprint, render_template, redirect, url_for, request, session, current_app

blueprint_member = Blueprint('member', __name__)

@blueprint_member.route('/member/', methods=['GET', 'POST'])
def member():
  if request.method == 'GET':
    if 'user_id' in session:
      cnx = current_app.db_cnx()
      cursor = cnx.cursor()
      cursor.execute('SELECT name FROM member WHERE username = %s', (session.get('user_id'), ))
      user_name = cursor.fetchone()
      cursor.close()
      cnx.close()
      return render_template('member.html', header_title = f"{user_name[0]}您好，這是會員頁")
    return redirect(url_for('index.index'))