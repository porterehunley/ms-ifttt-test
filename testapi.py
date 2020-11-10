from flask import Flask 
from flask import request, jsonify

app = Flask(__name__)

from triggers import bp as trigger_bp
from services import bp as service_bp
from actions import bp as action_bp

app.register_blueprint(trigger_bp, url_prefix='/ifttt/v1/triggers')
app.register_blueprint(service_bp, url_prefix='/services')
app.register_blueprint(action_bp, url_prefix='/ifttt/v1/actions')
service_key = "3aKjTXxu2zoRqxr1rZ5nkniI56JWOTo51gwgCu7hZfbxmkiVIJEt4e5q_E3lxEOL"

@app.route('/')
def index():
    return "hello world"

@app.route('/ifttt/v1/status', methods=['GET'])
def status():
    if ("IFTTT-Service-Key" not in request.headers or request.headers["IFTTT-Service-Key"] != service_key):
        return "", 401        
    return "", 200

@app.route('/ifttt/v1/test/setup', methods=['GET', 'POST'])
def setup():
    if ("IFTTT-Service-Key" not in request.headers or request.headers["IFTTT-Service-Key"] != service_key):
        return "", 401
           
    return jsonify({
        "data": {
            "samples": {
                "triggers": {
                    "new_date_created": {}
                }
            },
        }
    })

