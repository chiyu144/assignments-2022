import os
import mysql.connector
from mysql.connector import Error
from flask import Flask, g

from view.index import blueprint_index
from view.member import blueprint_member
from view.error import blueprint_error
from api.signup import blueprint_signup
from api.signin import blueprint_signin
from api.signout import blueprint_signout
from api.members import blueprint_members

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.secret_key = os.urandom(12).hex()

app.register_blueprint(blueprint_index)
app.register_blueprint(blueprint_member)
app.register_blueprint(blueprint_error)

app.register_blueprint(blueprint_signup, url_prefix = '/api')
app.register_blueprint(blueprint_signin, url_prefix = '/api')
app.register_blueprint(blueprint_signout, url_prefix = '/api')
app.register_blueprint(blueprint_members, url_prefix = '/api')

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

if __name__ =='__main__':
  app.run(port = 3000, debug = True)