from flask import Flask
app = Flask(__name__)
from flask import render_template, request, redirect, url_for
import os
import yaml

import profile
import scrapie

URL = "https://skypech.com"
UPLOAD_DIR = './static/wallpapers'
PROFILE = 'profile.yml'
USER_NAME = "rinanapop"

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        if ('file' in request.files):

            file = request.files['file']    
            if file.filename == '':
                return redirect(url_for('index'))
            
            file.save(os.path.join(UPLOAD_DIR, file.filename))

            with open(PROFILE, 'r+') as yf:
                profile = yaml.safe_load(yf)
                profile[USER_NAME]['wallpaper'] = file.filename
            with open(PROFILE, 'w') as yf:
                yf.write(str(profile))

            return redirect(url_for('index'))

        return render_template('calendar.html')

    else:
        with open(PROFILE, 'r') as yf:
            profile = yaml.load(yf)

        return render_template(
            'base.html',
            posts=scrapie.get_girls_posts_info(URL),
            wallpaper = profile[USER_NAME]['wallpaper'],
            colorscheme = profile[USER_NAME]['colorscheme']
        )
