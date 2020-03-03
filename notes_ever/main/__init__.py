import flask

main_bp = flask.Blueprint('main', __name__)

from notes_ever.main import routes
