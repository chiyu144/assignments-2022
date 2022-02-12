import mysql.connector
from mysql.connector import Error
import os
from flask import Flask, render_template, request, session, redirect, url_for, make_response, g

app = Flask(__name__)
app.secret_key = os.urandom(12).hex()

# Sign In: 檢查有無使用者 & 帳密對不對
def checkUser(user_id, password):
  g.cursor.execute('SELECT * FROM member WHERE username = %s', (user_id, ))
  user = g.cursor.fetchone()
  if user and password == user[3]:
    return True

# Sign Up: 檢查帳號是否重複
def validateId(user_id):
  g.cursor.execute('SELECT username FROM member')
  usernames = g.cursor.fetchall()
  for username in usernames:
    if user_id == username[0]:
      return True

# Sign Up: 新增使用者
def addUser(user_name, user_id, password):
  sql = 'INSERT INTO member (name, username, password) VALUES (%s, %s, %s)'
  val = (user_name, user_id, password)
  g.cursor.execute(sql, val)
  g.db.commit()

@app.before_request
def connection():
  try:
    db = mysql.connector.connect(
        host = 'localhost', port = '3306',
        user = 'root', password = 'qwert123',
        database = 'website'
      )
    if db.is_connected():
      g.db = db
      g.cursor = db.cursor()
  except Error as e:
    print('Connection Error: ', e)

@app.teardown_request
def closeDb(exc):
  if hasattr(g, 'cursor'):
    g.cursor.close()
  if hasattr(g, 'db'):
    g.db.close()

@app.route('/', methods=['GET'])
def index():
  response = make_response(render_template('index.html', header_title = '歡迎使用系統'))
  response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
  response.headers['Pragma'] = 'no-cache'
  return response

@app.route('/member/', methods=['GET'])
def member():
  if 'user_id' in session:
    return render_template('member.html', header_title = f"{session.get('user_id')}您好，這是會員頁")
  return redirect(url_for('index'))

@app.route('/error/')
def error():
  return render_template('error.html', header_title = '登入失敗', message = request.args.get('message'))

@app.route('/signup', methods=['POST'])
def signUp():
  if request.method == 'POST':
    user_name = request.get_json()['userName']
    user_id = request.get_json()['userId']
    password = request.get_json()['password']
    message = None
    if user_name and user_id and password:
      if validateId(user_id):
        message = '帳號已經被註冊'
        return redirect(url_for('error', header_title = '註冊失敗', message = message))
      else:
        addUser(user_name, user_id, password)
        return redirect(url_for('index'))
    else:
      message = '姓名、帳號、密碼皆不得為空'
      return redirect(url_for('error', header_title = '註冊失敗', message = message))

@app.route('/signin', methods=['POST'])
def signIn():
  if request.method == 'POST':
    user_id = request.get_json()['userId']
    password = request.get_json()['password']
    message = None
    if user_id and password:
      if checkUser(user_id, password):
        session.permanent = True
        session['user_id'] = user_id
        return redirect(url_for('member'))
      else:
        message = '帳號或密碼錯誤'
        return redirect(url_for('error', message = message))
    else:
      message = '帳號或密碼不得為空'
      return redirect(url_for('error', message = message))

@app.route('/signout', methods=['GET'])
def signOut():
  session.pop('user_id', None)
  session.clear()
  return redirect(url_for('index'))

if __name__ =='__main__':
  app.run(port = 3000, debug = True)