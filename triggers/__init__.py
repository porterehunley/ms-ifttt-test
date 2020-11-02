from flask import Blueprint

bp = Blueprint('triggers', __name__)

from triggers import routes, responses