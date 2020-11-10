import uuid

def create_action_response():
    return {
        'data': [
            {
                'id': uuid.uuid4()
            }
        ]
    }