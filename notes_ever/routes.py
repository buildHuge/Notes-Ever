import flask

from notes_ever import app

@app.route("/")
def index():
    return flask.render_template("index.html")
    