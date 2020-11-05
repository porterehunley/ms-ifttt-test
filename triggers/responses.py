import time
import uuid

def create_triggers_response(ingrediants):
    reponse = {"data": []}
    for i, ingrediant in enumerate(ingrediants):
        meta = {
            "id": uuid.uuid4(),
            "timestamp": int(time.time()) - i
        }
        reponse["data"].append({
            ingrediant[0]: ingrediant[1],
            "meta": meta
            })
    
    return reponse

def create_error_response(errors):
    return {
        "errors": errors
    }
