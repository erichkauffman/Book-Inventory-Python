from flask import Flask
from flask_socketio import SocketIO
import flask_cors

from routes.books import bookRoutes
from routes.items import itemRoutes
from routes.locations import locationRoutes
from routes.phrases import phraseRoutes

socketio = SocketIO()

def create_app():
	app = Flask(__name__)
	flask_cors.CORS(app=app)

	app.register_blueprint(bookRoutes, url_prefix='/books')
	app.register_blueprint(itemRoutes, url_prefix='/items')
	app.register_blueprint(locationRoutes, url_prefix='/locations')
	app.register_blueprint(phraseRoutes, url_prefix='/phrases')

	socketio.init_app(app)
	return app
