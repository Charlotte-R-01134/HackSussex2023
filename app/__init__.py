from flask import Flask
from .extensions import bootstrap, db, moment, login_manager
from config import config

def create_app():
    config_name = 'default'
    app = Flask(__name__) # set the application name
    app.config.from_object(config[config_name]) # load the config file
    config[config_name].init_app(app) # initialize the config file

    db.init_app(app) # initialize the database
    moment.init_app(app) # initialize the moment
    bootstrap.init_app(app) # initialize the bootstrap
    login_manager.init_app(app) # initialize the login manager

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint) # register the main blueprint

    from .auth import auth as auth__blueprint
    app.register_blueprint(auth__blueprint, url_prefix='/auth') # register the auth blueprint

    return app