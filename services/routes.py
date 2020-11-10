from services import bp
from flask import jsonify, request

@bp.route('/', methods=['GET'])
def get_services(name):
    return jsonify({"TODO": "TODO"}), 200

@bp.route('/triggers',)
def get_triggers_for_service():
    service = request.args.get('service', default = "", type = str)
    