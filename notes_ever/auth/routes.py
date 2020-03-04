import flask
from oauthlib.oauth2 import WebApplicationClient
import os

from notes_ever.auth import auth_bp
from notes_ever.auth import helpers

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
client = WebApplicationClient(GOOGLE_CLIENT_ID)


@auth_bp.route("/student-login")
def login():
    
    # Get authorization_endpoint from google's discovery document
    authorization_endpoint = helpers.get_google_discovery_config()["authorization_endpoint"]

    # Construct the URL to which end users will be sent by this route
    request_uri = client.prepare_request_uri(
        authorization_endpoint, 
        redirect_uri=flask.request.base_url + "/callback",
        scope=["openid", "email"]
        )

    # User reached via GET, render login.html 
    return flask.redirect(request_uri)

@auth_bp.route("/student-login/callback")
def callback():
    return flask.redirect(url_for("main.index"))
