from flask import Blueprint

bp = Blueprint('actions', __name__)

from actions import routes, responses