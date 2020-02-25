import flask

auth = flask.Blueprint('Auth',__name__)

@auth.route("/login")
def login():
    return flask.render_template("login.html")
