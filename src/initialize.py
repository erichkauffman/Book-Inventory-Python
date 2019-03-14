from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()

def create_app():
	app = Flask(__name__)
	app.debug = True

	socketio.init_app(app)
	return app
