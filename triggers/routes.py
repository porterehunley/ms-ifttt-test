from triggers import bp
from flask import request, jsonify
from datetime import datetime, timedelta
from triggers.responses import create_triggers_response, create_error_response

'''
trigger body:
+ trigger_identity(string) - a unique identifier for a specific user's trigger. IFTTT
  recomends some relationship is stored on our part.
+ triggerFields(Map) - see docs
+ limit(int) - limit number of 'ingrediants' returned 
+ user - info on user -> not used in the trigger's opp, don't think they need it
+ ifttt_source - info on applet
'''
service_key = "3aKjTXxu2zoRqxr1rZ5nkniI56JWOTo51gwgCu7hZfbxmkiVIJEt4e5q_E3lxEOL"
@bp.route('/new_date_created', methods=['POST', 'GET'])
def new_date_created():
	try:
		data = request.get_json() or {}
		if ("IFTTT-Service-Key" not in request.headers or request.headers["IFTTT-Service-Key"] != service_key):
			return create_error_response(["service key not valid"]), 401
		
		limit = data['limit'] if 'limit' in data else 50
		ingrediants = [("date", (datetime.now()-timedelta(minutes=x)).isoformat()) for x in range(limit)]
		return jsonify(create_triggers_response(ingrediants))
	
	except Exception as e:
		return create_error_response([e]), 500
