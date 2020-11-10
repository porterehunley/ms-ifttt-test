from actions import bp
from actions.responses import create_action_response
from flask import request, jsonify
from datetime import datetime, timedelta

'''
actionFields
'''
@bp.route('/create_new_name')
def create_new_date():
    data = request.get_json() or {}
    actionFields = data['actionFields']
    with open('user_names.txt', 'a') as f:
        f.write(actionFields['name'])
    f.close()

    return jsonify(create_action_response()), 200
    