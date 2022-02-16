import os
import mysql.connector
from mysql.connector import Error
import configparser
from flask import Flask, g

from view.index import blueprint_index
from view.member import blueprint_member
from view.error import blueprint_error
from model.signup import blueprint_signup
from model.signin import blueprint_signin
from model.signout import blueprint_signout
from api.member import blueprint_member_api
from api.members import blueprint_members_api

config = configparser.ConfigParser()
config.read('config.ini')

app = Flask(__name__)

app.config['ENV'] = config['App']['env']
app.config['JSON_AS_ASCII'] = config['App'].getboolean('json_as_ascii')

app.secret_key = os.urandom(12).hex()

app.register_blueprint(blueprint_index)
app.register_blueprint(blueprint_member)
app.register_blueprint(blueprint_error)

app.register_blueprint(blueprint_signup)
app.register_blueprint(blueprint_signin)
app.register_blueprint(blueprint_signout)

app.register_blueprint(blueprint_member_api, url_prefix = '/api')
app.register_blueprint(blueprint_members_api, url_prefix = '/api')

@app.before_request
def connection():
  try:
    db = mysql.connector.connect(
        host = config['Mysql']['host'],
        port = int(config['Mysql']['port']),
        user = config['Mysql']['user'],
        password = config['Mysql']['password'],
        database = config['Mysql']['database']
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