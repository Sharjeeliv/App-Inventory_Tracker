from flask import Flask, url_for
from routes import routes

app = Flask(__name__)  # Created app
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run()

