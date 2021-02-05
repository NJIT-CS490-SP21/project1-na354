import requests
import os
import random
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

Artists = ['66CXWjxzNUsdJxJ2JdwvnR', '4NHQUGzhtTLFvgF5SZesLK', '6M2wZ9GZgrQXHCFfjv46we']
songs = [0,1,2,3,4,5,6,7,8,9]

RandomID = random.choice(Artists)


BASE_URL = 'https://api.spotify.com/v1/'

ARTIST_URL = 'https://api.spotify.com/v1/artists/'

tracks = '/top-tracks?market=US'


r = requests.get((ARTIST_URL + RandomID + tracks), headers=headers)

test =r.json()
print(test['tracks'][random.choice(songs)]['name'])