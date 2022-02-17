from flask import Blueprint, render_template, redirect, url_for, request, session, current_app
from decorators import with_cnx

blueprint_member = Blueprint('member', __name__)

@with_cnx(need_commit = False)
def queryMemberName(cursor, user_id):
  cursor.execute('SELECT name FROM member WHERE username = %s', (user_id, ))
  user_name = cursor.fetchone()
  return user_name[0]

@blueprint_member.route('/member/', methods=['GET', 'POST'])
def member():
  if request.method == 'GET':
    if 'user_id' in session:
      # cnx = current_app.db_cnx()
      # cursor = cnx.cursor()
      # cursor.execute('SELECT name FROM member WHERE username = %s', (session.get('user_id'), ))
      # user_name = cursor.fetchone()
      # cursor.close()
      # cnx.close()
      return render_template('member.html', header_title = f"{queryMemberName(session.get('user_id'))}您好，這是會員頁")
    return redirect(url_for('index.index'))