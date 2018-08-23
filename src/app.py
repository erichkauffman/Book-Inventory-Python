from flask import Flask
from routes.books import bookRoutes

app = Flask(__name__)

@app.route('/')
def index():
    return("Hello!")

app.register_blueprint(bookRoutes, url_prefix='/books')

if __name__ == '__main__':
    app.run(host='0.0.0.0')