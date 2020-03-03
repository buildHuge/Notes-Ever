import flask

from notes_ever.main import main_bp

@main_bp.route("/")
def index():
    return flask.render_template("index.html")
    