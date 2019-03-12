from initialize import create_app, socketio
from lib.response import makeJsonResponse

app = create_app()

@app.route('/')
def index():
    return "Hello!"

@app.errorhandler(404)
def notFound(e):
	return makeJsonResponse({"success": False, "message": "not found"}), 404

@app.errorhandler(405)
def notAllowed(e):
	return makeJsonResponse({"success": False, "message": "method not implemented"}), 405

@app.errorhandler(500)
def internalError(e):
	return makeJsonResponse({"success": False, "message": "something went wrong"}), 500

if __name__ == '__main__':
    socketio.run(app=app, host='0.0.0.0')
