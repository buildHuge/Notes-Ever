import os
import tempfile

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """All the configurations required to run the web application"""

    # Set SECRET_KEY to sign cookies and for other security related tools
    SECRET_KEY = os.environ.get("SECRET_KEY")

    # Turn on Jinja template reloading
    TEMPLATES_AUTO_RELOAD = True

    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or ("sqlite:///" + os.path.join(basedir, "Notes-Ever.db"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
