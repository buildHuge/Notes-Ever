import flask
import os
import json
import requests
from oauthlib.oauth2 import WebApplicationClient

from notes_ever.auth import auth_bp
from notes_ever.auth import helpers

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")
client = WebApplicationClient(GOOGLE_CLIENT_ID)


@auth_bp.route("/student-login")
def login():
    
    # Get authorization_endpoint from google's discovery document
    authorization_endpoint = helpers.get_google_discovery_config()["authorization_endpoint"]

    # Construct the URL to which end users will be sent by this route
    request_uri = client.prepare_request_uri(
        authorization_endpoint, 
        redirect_uri=flask.request.base_url + "/callback",
        scope=["openid", "email"],
        hd="ssipmt.com"
        )

    # User reached via GET, render login.html 
    return flask.redirect(request_uri)


@auth_bp.route("/student-login/callback")
def callback():

    # Get authorization code from URL query 
    code = flask.request.args.get("code")
    google_disc_config = helpers.get_google_discovery_config()
    token_endpoint = google_disc_config["token_endpoint"]
    
    # Preparing for exchanging code to token
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=flask.request.url,
        redirect_url=flask.request.base_url,
        code=code
    )
    
    # Response from exchanging Code 
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    # Parse the tokens
    client.parse_request_body_response(json.dumps(token_response.json()))

    # Now that we have tokens (yay) let's find and hit URL
    # from Google that gives you user's profile information,
    # including their Google Profile Image and Email
    userinfo_endpoint = google_disc_config["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    # We want to make sure their email is verified.
    # The user authenticated with Google, authorized our
    # app, and now we've verified their email through Google!
    unique_id = userinfo_response.json()["sub"]
    users_email = userinfo_response.json()["email"]

    print(unique_id, users_email)

    return flask.redirect(flask.url_for("main.index"))
