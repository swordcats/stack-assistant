"""
This module creates an authorization token if one doesn't exist already.
"""

import requests
from tokens import *
import base64

def get_auth():
    authOptions = {
        'url': 'https://accounts.spotify.com/api/token',
        'headers': {
            'Authorization': 'Basic ' + base64.b64encode((CLIENT_ID + ':' + CLIENT_SECRET).encode()).decode()
        },
        'form': {
            'grant_type': 'client_credentials'
        },
        'json': True
    }

    response = requests.post(authOptions['url'], headers = authOptions['headers'], data = authOptions['form'])

    if response.status_code == 200:
        body = response.json()
        token = body['access_token']

        file = open("api_spotify/auth_token.py", "w")
        file.write(f"TOKEN = '{token}'")
        file.close()

        return token
    
__all__ = [get_auth.__name__]