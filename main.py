from flask import Flask
app = Flask(__name__)
from flask import render_template, request, redirect, url_for
import os
import yaml

import config
import profile
import scrapie

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        if ('file' in request.files):

            file = request.files['file']    
            if file.filename == '':
                return redirect(url_for('index'))
            
            file.save(os.path.join(config.UPLOAD_DIR, file.filename))

            with open(config.PROFILE, 'r+') as yf:
                profile = yaml.safe_load(yf)
                profile[config.USER_NAME]['wallpaper'] = file.filename
            with open(config.PROFILE, 'w') as yf:
                yf.write(str(profile))

            return redirect(url_for('index'))

        return render_template('calendar.html')

    else:
        with open(config.PROFILE, 'r') as yf:
            profile = yaml.load(yf)

        return render_template(
            'base.html',
            posts=scrapie.get_girls_posts_info(config.URL),
            wallpaper = profile[config.USER_NAME]['wallpaper'],
            colorscheme = profile[config.USER_NAME]['colorscheme']
        )

@app.route('/get_more_posts', methods=['POST'])
def get_more_posts():
    posts = scrapie.get_girls_posts_info(config.URL_ID + request.form.get('id'))

    return render_template(
        'more_posts.html',
        posts=posts
    )
