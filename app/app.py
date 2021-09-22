from flask import Flask, render_template
from routes import path

def create_app():
    app = Flask(__name__)
    app.secret_key = 'rd'
    app.register_blueprint(path)

    return app