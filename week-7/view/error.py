from flask import Blueprint, render_template, request

error = Blueprint('error', __name__)

@error.route('/error/')
def error():
  return render_template('error.html', header_title = '登入失敗', message = request.args.get('message'))