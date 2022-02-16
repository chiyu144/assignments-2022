from flask import Blueprint, redirect, url_for, session

signout = Blueprint('signout', __name__)

@signout.route('/signout', methods=['GET'])
def signOut():
  session.pop('user_id', None)
  session.clear()
  return redirect(url_for('index'))