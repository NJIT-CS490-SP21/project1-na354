import os
import random
import flask
from project1 import getArtist, getTrack

app = flask.Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def startflask():
    song = getTrack()
    prev  = ''
    if (song[0]['preview_url']):
        prev = song[0]['preview_url']
    #print(song[1])
    #print(song[0]["name"])
    return flask.render_template("index.html", image = song[0]['album']['images'][0]['url'], name = song[0]["name"], artist = song[0]["album"]["artists"][0]["name"], preview = prev, lyrics = song[1]['response']['hits'][0]['result']['url'] )

app.run(
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080))
    )