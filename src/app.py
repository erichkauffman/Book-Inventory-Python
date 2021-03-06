from initialize import create_app, socketio
from lib.response import makeJsonResponse
from routes.books import bookRoutes
from routes.items import itemRoutes
from routes.sites import siteRoutes
from routes.savedData import savedDataRoutes
from routes.issues import issueRoutes
import flask_cors
import os

app = create_app()
flask_cors.CORS(app=app)

app.register_blueprint(bookRoutes, url_prefix='/books')
app.register_blueprint(itemRoutes, url_prefix='/items')
app.register_blueprint(siteRoutes, url_prefix='/sites')
app.register_blueprint(savedDataRoutes, url_prefix='/savedData')
app.register_blueprint(issueRoutes, url_prefix='/issues')

@app.route('/')
def index():
    return f"Hello, {os.environ['APIENV']}!"

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
