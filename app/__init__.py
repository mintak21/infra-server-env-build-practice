import os

from flask import Flask

from .config import config_map
from .database import init_db


def create_app(config_use='development'):
    app = Flask(__name__, root_path=os.path.dirname(__file__))
    app.config.from_object(config_map[config_use])
    init_db(app)

    return app
