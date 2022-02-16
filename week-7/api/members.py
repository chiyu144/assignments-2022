from flask import Blueprint

members = Blueprint('members', __name__)

@members.route('/members')
def members():
  return 'YOOOOOOOOOOO members'