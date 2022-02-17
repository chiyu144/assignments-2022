from flask import Blueprint, redirect, url_for, request
from decorators import with_cnx

blueprint_signup = Blueprint('signup', __name__)

# 檢查帳號是否重複
@with_cnx(need_commit = False)
def validateId(cursor, user_id):
  cursor.execute('SELECT count(username) FROM member WHERE username = %s', (user_id, ))
  username = cursor.fetchone()
  if username[0] > 0:
    return True

# def validateId(user_id):
#   cnx = current_app.db_cnx()
#   cursor = cnx.cursor()
#   cursor.execute('SELECT count(username) FROM member WHERE username = %s', (user_id, ))
#   username = cursor.fetchone()
#   cursor.close()
#   cnx.close()
#   if username[0] > 0:
#     return True

# @current_app.with_cnx(need_commit = False)
# def validateId(cursor, user_id):
#   cursor.execute('SELECT count(username) FROM member WHERE username = %s', (user_id, ))
#   username = cursor.fetchone()
#   if username[0] > 0:
#     return True

# 新增使用者
@with_cnx(need_commit = True)
def addUser(cursor, user_name, user_id, password):
  sql = 'INSERT INTO member (name, username, password) VALUES (%s, %s, %s)'
  val = (user_name, user_id, password)
  cursor.execute(sql, val)

# def addUser(user_name, user_id, password):
#   cnx = current_app.db_cnx()
#   cursor = cnx.cursor()
#   sql = 'INSERT INTO member (name, username, password) VALUES (%s, %s, %s)'
#   val = (user_name, user_id, password)
#   cursor.execute(sql, val)
#   cnx.commit()
#   cursor.close()
#   cnx.close()

@blueprint_signup.route('/signup', methods=['POST'])
def signUp():
  if request.method == 'POST':
    user_name = request.get_json()['userName']
    user_id = request.get_json()['userId']
    password = request.get_json()['password']
    message = None
    if user_name and user_id and password:
      if validateId(user_id):
        message = '帳號已經被註冊'
        return redirect(url_for('error.error', header_title = '註冊失敗', message = message))
      else:
        addUser(user_name, user_id, password)
        return redirect(url_for('index.index'))
    else:
      message = '姓名、帳號、密碼皆不得為空'
      return redirect(url_for('error.error', header_title = '註冊失敗', message = message))