from flask import Flask
from .site.routes import site
from .authentication.routes import auth
from config import Config
from flask_migrate import Migrate

from .models import db as root_db, login_manager, ma

app = Flask(__name__)

app.register_blueprint(site)
app.config.from_object(Config)
app.register_blueprint(auth)

root_db.init_app(app)

migrate = Migrate(app, root_db)
login_manager.init_app(app)
login_manager.login_view = 'auth.signin'
ma.init_app(app)
