from flask import Blueprint, redirect, url_for, request, session
from decorators import with_cnx

blueprint_signin = Blueprint('signin', __name__)

# 檢查有無使用者 & 帳密對不對
@with_cnx(need_commit = False)
def checkUser(cursor, user_id, password):
  cursor.execute('SELECT username, password FROM member WHERE username = %s', (user_id, ))
  user = cursor.fetchone()
  if user and password == user[1]:
    return True

@blueprint_signin.route('/signin', methods=['POST'])
def signIn():
  if request.method == 'POST':
    user_id = request.get_json()['userId']
    password = request.get_json()['password']
    message = None
    if user_id and password:
      if checkUser(user_id, password):
        session.permanent = True
        session['user_id'] = user_id
        return redirect(url_for('member.member'))
      else:
        message = '帳號或密碼錯誤'
        return redirect(url_for('error.error', message = message))
    else:
      message = '帳號或密碼不得為空'
      return redirect(url_for('error.error', message = message))