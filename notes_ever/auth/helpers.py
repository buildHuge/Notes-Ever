import requests

def get_google_discovery_config():
    """Fetching google's discovery document (open-id configuration)"""
    
    return requests.get("https://accounts.google.com/.well-known/openid-configuration").json()
