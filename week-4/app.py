from flask import Flask, render_template, request, session, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(12).hex()

@app.route('/')
def index ():
  return render_template('index.html', header_title = '歡迎光臨，請輸入帳號密碼')

@app.route('/member/')
def member ():
  if 'user_id' in session: 
    return render_template('member.html', header_title = '歡迎光臨，這是會員頁')
  return redirect(url_for('index'))

@app.route('/error/')
def error ():
  return render_template('error.html', header_title = '失敗頁面')

@app.route('/signin', methods=['POST'])
def signIn ():
  if request.method == 'POST':
    user_id = request.get_json()['userId']
    password = request.get_json()['password']
    message = None
    if user_id and password:
      if user_id == 'test' and password == 'test':
        session.permanent = True
        session['user_id'] = user_id 
        return redirect(url_for('member'))
      else:
        message = '帳號、或密碼輸入錯誤'
        return redirect(url_for('error', message = message))
    else:
      message = '請輸入帳號、密碼'
      return redirect(url_for('error', message = message))

@app.route('/signout')
def signOut ():
  session.pop('user_id', None)
  session.clear()
  return redirect(url_for('index'))

if __name__ =='__main__':
  # debug 模式，可以 Hot Reload + 報錯會顯示在瀏覽器上
  # port 預設是 5000，依照作業要求改成 3000
  app.run(port = 3000, debug = True)