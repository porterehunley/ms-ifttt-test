from flask import Blueprint

bp = Blueprint('services', __name__)

from triggers import routes, responses, ifttt