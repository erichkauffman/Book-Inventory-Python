import json

def createStatus(status: int, success=False, reason="none"):
    return (json.dumps({"success": success, "reason": reason}), status, {"ContentType": "application/json"})

