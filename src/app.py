from flask import Flask
from flask_socketio import SocketIO
import flask_cors

from routes.books import bookRoutes
from routes.items import itemRoutes
from routes.locations import locationRoutes
from routes.phrases import phraseRoutes
from lib.response import makeJsonResponse

app = Flask(__name__)
socketio = SocketIO(app)
flask_cors.CORS(app=app)

@app.route('/')
def index():
    return "Hello!"

app.register_blueprint(bookRoutes, url_prefix='/books')
app.register_blueprint(itemRoutes, url_prefix='/items')
app.register_blueprint(locationRoutes, url_prefix='/locations')
app.register_blueprint(phraseRoutes, url_prefix='/phrases')

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
