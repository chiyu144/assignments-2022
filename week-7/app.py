import os
import mysql.connector
from mysql.connector import Error
from flask import Flask, g

from view.index import index
from view.member import member
from view.error import error
from api.signup import signup
from api.signin import signin
from api.signout import signout
from api.members import members

app = Flask(__name__)
app.secret_key = os.urandom(12).hex()
app.register_blueprint(index)
app.register_blueprint(member)
app.register_blueprint(error)
app.register_blueprint(signup)
app.register_blueprint(signin)
app.register_blueprint(signout)
app.register_blueprint(members)

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
  app.run(port = 3000)