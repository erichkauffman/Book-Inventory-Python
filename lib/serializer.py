import json

def serialize(obj):
    if isinstance(obj, list):
        return json.dumps([o.__dict__ for o in obj])
    else:
        return json.dumps(obj.__dict__)