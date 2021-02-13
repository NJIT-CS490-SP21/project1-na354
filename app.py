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
    if (song['preview_url']):
        prev = song['preview_url']
        
    print(song["name"])
    return flask.render_template("index.html", image = song['album']['images'][0]['url'], name = song["name"], artist = song["album"]["artists"][0]["name"], id = song["id"], preview = prev)

app.run(
    port=int(os.getenv('PORT', 8080))
    )