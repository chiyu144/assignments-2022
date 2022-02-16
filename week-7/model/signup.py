from flask import Blueprint, redirect, url_for, request, g

blueprint_signup = Blueprint('signup', __name__)

# 檢查帳號是否重複
def validateId(user_id):
  g.cursor.execute('SELECT count(username) FROM member WHERE username = %s', (user_id, ))
  username = g.cursor.fetchone()
  if username[0] > 0:
    return True

# 新增使用者
def addUser(user_name, user_id, password):
  sql = 'INSERT INTO member (name, username, password) VALUES (%s, %s, %s)'
  val = (user_name, user_id, password)
  g.cursor.execute(sql, val)
  g.db.commit()

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