import flask
import flask_sqlalchemy
import flask_login
import flask_migrate
import config 

from notes_ever.auth import auth_bp
from notes_ever.main import main_bp

##initializes the app
app = flask.Flask(__name__)


##register-Blueprints
app.register_blueprint(main_bp)
app.register_blueprint(auth_bp)

##configuers the app
app.config.from_object(config.Config)

##initializes the database
db = flask_sqlalchemy.SQLAlchemy(app)

##configuers database so that we can migrate our models
migrate = flask_migrate.Migrate(app, db)

##imports the main routes of the app
from notes_ever.auth import routes
from notes_ever.main import routes
