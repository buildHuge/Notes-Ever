import flask

from notes_ever.auth import auth_bp

@auth_bp.route("/login")
def login():
    return flask.render_template("login.html")
#google client id : 255112281279-l7uht2ekdbhcr1bos7u8qthv290mel7t.apps.googleusercontent.com
#google secret id : 0ZpF0XGXLV2lD5TcEuhWH1Vs
