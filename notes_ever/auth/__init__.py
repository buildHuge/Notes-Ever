import flask

auth_bp = flask.Blueprint('auth', __name__)

from notes_ever.auth import routes
