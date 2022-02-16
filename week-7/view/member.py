from flask import Blueprint, render_template, redirect, url_for, session, g

member = Blueprint('member', __name__)

@member.route('/member/', methods=['GET'])
def member():
  if 'user_id' in session:
    g.cursor.execute('SELECT username FROM member WHERE username = %s', (session.get('user_id'), ))
    user = g.cursor.fetchone()
    return render_template('member.html', header_title = f"{user[1]}您好，這是會員頁")
  return redirect(url_for('index'))