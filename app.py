import os
import random
import flask
from project1 import getArtist, getTrack

app = flask.Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def hello_world():
    test = getTrack()
    prev  = ''
    if (test['preview_url']):
        prev = test['preview_url']
    
    return flask.render_template("index.html", image = test['album']['images'][0]['url'], name = test["name"], artist = test["album"]["artists"][0]["name"], id = test["id"], preview = prev)

app.run(
    port=int(os.getenv('PORT', 8080))
    )
