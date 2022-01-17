from flask import Flask, render_template, jsonify, request, session, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index ():
  return render_template('index.html', header_title = '歡迎光臨，請輸入帳號密碼')

@app.route('/signin', methods=['POST'])
def signIn ():
  return render_template('member.html')

if __name__ =='__main__':
  # debug 模式，可以 Hot Reload + 報錯會顯示在瀏覽器上
  # port 預設是 5000，依照作業要求改成 3000
  app.run(port = 3000, debug = True)