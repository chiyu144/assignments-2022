import os
from mysql.connector import Error, pooling
import configparser
# from functools import wraps
from flask import Flask, current_app

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

def create_db_pool():
  return pooling.MySQLConnectionPool(
    pool_name = config['Mysql']['pool_name'],
    pool_size = int(config['Mysql']['pool_size']),
    host = config['Mysql']['host'],
    port = int(config['Mysql']['port']),
    user = config['Mysql']['user'],
    password = config['Mysql']['password'],
    database = config['Mysql']['database']
  )

def db_cnx():
  try:
    cnx = current_app.db_pool.get_connection()
    if cnx.is_connected():
      return cnx
  except Error as e:
    print('MySql Connection Pool error: ', e)

# def sql_execution(need_commit = None):
#   def decorator(func):
#     @wraps(func)
#     def decorated_func(*args, **kwargs):
#       try:
#         func(*args, **kwargs)
#         if need_commit:
#           cnx.commit()
#       except Error as e:
#         print('MySql Connection Pool error: ', e)
#       finally:
#         cursor.commit()
#         cnx.close()
#     return decorated_func
#   return decorator

app = Flask(__name__)
with app.app_context():
  current_app.db_pool = create_db_pool()
  current_app.db_cnx = db_cnx
  # current_app.sql_execution = sql_execution

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

# @app.teardown_request
# def closeDb(exc):
#   if hasattr(g, 'cursor'):
#     g.cursor.close()
#   if hasattr(g, 'db'):
#     g.db.close()

if __name__ =='__main__':
  app.run(port = 3000, debug = True)