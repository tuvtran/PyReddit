from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# local import
from instance.config import app_config

# initialize the db instance
db = SQLAlchemy()

# initialize bcrypt
bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    db.init_app(app)
    bcrypt.init_app(app)

    # import blueprints here
    from app.views import views_bp

    # import models
    from app import models      # noqa

    app.register_blueprint(views_bp)

    return app
