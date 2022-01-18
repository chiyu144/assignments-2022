from flask import Flask, render_template, request, session, redirect, url_for, make_response
import os

app = Flask(__name__)
app.secret_key = os.urandom(12).hex()

@app.route('/')
def index ():
  response = make_response(render_template('index.html', header_title = '歡迎使用系統'))
  response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
  response.headers['Pragma'] = 'no-cache'
  return response

@app.route('/member/')
def member ():
  if 'user_id' in session: 
    return render_template('member.html', header_title = f"您好 {session.get('user_id')} 君，這是會員頁")
  return redirect(url_for('index'))

@app.route('/error/')
def error ():
  if 'user_id' in session:
    return redirect(url_for('member'))
  return render_template('error.html', header_title = '登入失敗')

@app.route('/signin', methods=['POST'])
def signIn ():
  if request.method == 'POST':
    user_id = request.get_json()['userId']
    password = request.get_json()['password']
    message = None
    if user_id and password:
      if user_id == 'test' and password == 'test':
        # 預設 31 天後自動失效
        session.permanent = True
        # user_id 記錄起來
        session['user_id'] = user_id 
        return redirect(url_for('member'))
      else:
        message = '帳號或密碼錯誤'
        return redirect(url_for('error', message = message))
    else:
      message = '帳號或密碼不得為空'
      return redirect(url_for('error', message = message))

@app.route('/signout')
def signOut ():
  # 刪除資料 + 清除 session
  session.pop('user_id', None)
  session.clear()
  return redirect(url_for('index'))

if __name__ =='__main__':
  # debug 模式，可以 Hot Reload + 報錯會顯示在瀏覽器上
  # port 預設是 5000，依照作業要求改成 3000
  app.run(port = 3000, debug = True)