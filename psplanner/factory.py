import logging
from logging.config import dictConfig

import quart_flask_patch
from quart import Quart
from quart_session import Session
from flask_sqlalchemy import SQLAlchemy

from psplanner import config
from psplanner import logs


db = SQLAlchemy()

def create_app():
    from psplanner import filters
    from psplanner.cli import main as cli
    # from psplanner.routes import auth
    from psplanner.routes import main
    app = Quart(__name__)
    app.config.from_envvar("FLASK_SECRETS", "config.py")
    app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SESSION_TYPE"] = "redis"
    app.config["SESSION_PROTECTION"] = True
    db.init_app(app)
    Session(app)
    app.register_blueprint(cli.bp)
    dictConfig(config.LOGGING_CONFIG)

    if config.LOG_DIRECTORY:
        logs.configure_logging()

    @app.before_serving
    async def startup():
        app.register_blueprint(filters.bp)
        app.register_blueprint(main.bp)
        # app.register_blueprint(auth.bp)

    return app
