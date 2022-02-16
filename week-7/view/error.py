from flask import Blueprint, render_template, request

blueprint_error = Blueprint('error', __name__)

@blueprint_error.route('/error/')
def error():
  return render_template('error.html', header_title = '登入失敗', message = request.args.get('message'))