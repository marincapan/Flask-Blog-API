from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

cujes_app = Flask(__name__)
cujes_app.config.from_object(Config)
# disable fsqla's event system - unused, but if wastes resources if enabled
# more info: https://stackoverflow.com/questions/33738467/how-do-i-know-if-i-can-disable-sqlalchemy-track-modifications
cujes_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(cujes_app)
migrate = Migrate(cujes_app, db)

from cujes import routes  # noqa
# noqa makes flake8 ignore the PEP-8-non-compliant import
