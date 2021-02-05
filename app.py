import os
import random
from flask import Flask, render_template
from project1 import getArtist, getTrack

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def hello_world():
    test = getTrack()
    return test, test

app.run(
    port=int(os.getenv('PORT', 8080))
    )
