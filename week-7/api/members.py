from flask import Blueprint

blueprint_members = Blueprint('members', __name__)

@blueprint_members.route('/members')
def members():
  return 'YOOOOOOOOOOO members'