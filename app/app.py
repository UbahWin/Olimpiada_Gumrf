from flask import Flask
# from flask_bootstrap import Bootstrap
# from flask_sqlalchemy import SQLAlchemy

from routes import path
# from models import db

def create_app():
    app = Flask(__name__)
    app.secret_key = 'rd'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///bachelorproject'
    app.register_blueprint(path)
    # db.init_app(app)
    # bootstrap = Bootstrap(app)

    return app