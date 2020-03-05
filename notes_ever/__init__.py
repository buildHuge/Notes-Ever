import flask
import flask_sqlalchemy
import flask_migrate
import config 

# Initializes the app
app = flask.Flask(__name__)

# Configures the app
app.config.from_object(config.Config)

# Register blueprints
from notes_ever.auth import auth_bp
from notes_ever.main import main_bp

app.register_blueprint(main_bp)
app.register_blueprint(auth_bp)

# Initializes the database and migration
db = flask_sqlalchemy.SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)

# Import models
from notes_ever import models
