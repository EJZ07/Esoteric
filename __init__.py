from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

# def create_app():

#     init = Flask(__name__)

#     init.config['SECRET_KEY'] = 'secret-key-goes-here'
#     init.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

#     db.init_app(init)

#     # from .app import app as main_blueprint
#     # app.register_blueprint(main_blueprint)

#     return init