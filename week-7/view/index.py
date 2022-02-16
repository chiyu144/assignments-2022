from flask import Blueprint, make_response, render_template

blueprint_index = Blueprint('index', __name__)

@blueprint_index.route('/', methods=['GET'])
def index():
  response = make_response(render_template('index.html', header_title = '歡迎使用系統'))
  response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
  response.headers['Pragma'] = 'no-cache'
  return response