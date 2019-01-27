import os
from flask import Flask, render_template, request, redirect, url_for
from mutagen.mp3 import MP3 as mp3
import pygame
import time
import tests as notify
from numpy.random import *
import subprocess
from requests_oauthlib import OAuth1Session
import json
from pprint import pprint
def button_click():
    pygame.mixer.music.stop()
    window.destroy()
twitter = OAuth1Session("rtBqvvWEXYdMBTFl9ySsNBFFC", "FFb1t7XvY3jgJPnEaP8swErIhD9fNTVzkB7Ip64nCgKuFMyoA2", "717955109871706113-4OUizAlW6sVwm5QcNmT18D1E5tRvLRj", "yeMj6B4olwtKUhlga4myFTUeOZflxTZPfJdrVGgYEhbog")


app = Flask(__name__)

@app.route('/webhook/http://twitter.com/EqAlarm/status/<text>', methods=['GET', 'POST'])
def index(text):
    title = "Hi"
    it = text.replace("!#http://twitter.com/honkeasari_eew/status/","")
    params = {"id":it}
    req = twitter.get("https://api.twitter.com/1.1/statuses/show.json", params = params)

    timeline = json.loads(req.text)
    if timeline["text"].find("(終)") != -1:
        print("PTA")
        print(timeline["text"])
        cmd = "python window.py "+str(timeline["text"]).replace("\n",":pp:")
        returncode = subprocess.Popen(cmd, shell=True)
        cmd = "python whats.py "+str(timeline["text"]).replace("\n",":pp:")
        returncode = subprocess.Popen(cmd, shell=True)
    return render_template('./index.html')


if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0',port=618) 

