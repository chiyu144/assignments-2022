from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index ():
  return render_template('index.html', header_title = '歡迎光臨，請輸入帳號密碼')

@app.route('/member/')
def member ():
  return render_template('member.html', header_title = '歡迎光臨，這是會員頁')

@app.route('/error/')
def error ():
  return render_template('error.html', header_title = '失敗頁面')

@app.route('/signin', methods=['POST'])
def signIn ():
  if request.method =='POST':
    userId = request.get_json()['userId']
    password = request.get_json()['password']
    message = None
    if userId and password:
      if userId == 'test' and password == 'test':
        return redirect(url_for('member'))
      else:
        message = '帳號、或密碼輸入錯誤'
        return redirect(url_for('error', message = message))
    else:
      message = '請輸入帳號、密碼'
      return redirect(url_for('error', message = message))

@app.route('/signout')
def signOut ():
  return redirect(url_for('index'))

if __name__ =='__main__':
  # debug 模式，可以 Hot Reload + 報錯會顯示在瀏覽器上
  # port 預設是 5000，依照作業要求改成 3000
  app.run(port = 3000, debug = True)