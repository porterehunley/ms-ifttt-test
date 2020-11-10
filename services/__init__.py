from flask import Blueprint

bp = Blueprint('services', __name__)

from services import routes, responses, ifttt