import flask
import flask_sqlalchemy
import flask_login
import flask_migrate
import config 

from notes_ever.site.routes import main
from notes_ever.site.Auth import auth

##initializes the app
app = flask.Flask(__name__)

##register-Blueprints
app.register_blueprint(main)
app.register_blueprint(auth)

##configuers the app
app.config.from_object(config.Config)

##initializes the database
db = flask_sqlalchemy.SQLAlchemy(app)

##configuers database so that we can migrate our models
migrate = flask_migrate.Migrate(app, db)

##imports the main routes of the app
from notes_ever.site import Auth
from notes_ever.site import routes
