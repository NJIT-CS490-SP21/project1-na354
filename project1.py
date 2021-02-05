import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

CLIENT_ID = os.getenv('Client_ID')
CLIENT_SECRET = os.getenv('Client_Secret')
AUTH_URL = 'https://accounts.spotify.com/api/token'

auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

auth_response_data = auth_response.json()

access_token = auth_response_data['access_token']

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}


BASE_URL = 'https://api.spotify.com/v1/'

