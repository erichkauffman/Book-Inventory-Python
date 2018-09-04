from flask import Flask
from routes.books import bookRoutes
from routes.items import itemRoutes

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello!"

app.register_blueprint(bookRoutes, url_prefix='/books')
app.register_blueprint(itemRoutes, url_prefix='/items')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
