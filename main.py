from flask import Flask
app = Flask(__name__)
from flask import render_template, request, redirect, url_for
import os
import yaml

import config
import scrapie
import mod_conf

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        if ('file' in request.files):

            file = request.files['file']    
            if file.filename == '':
                return redirect(url_for('index')) # want to change to flash
            
            file.save(os.path.join(config.UPLOAD_DIR, file.filename))
            mod_conf.update('wallpaper', file.filename)

        else:
            new_colorscheme = request.form.get('colorscheme')
            mod_conf.update('colorscheme', new_colorscheme)

        return redirect(url_for('index'))

    else:
        with open(config.PROFILE, 'r') as yf:
            profile = yaml.safe_load(yf)

        return render_template(
            'base.html',
            posts=scrapie.get_girls_posts_info(config.URL),
            wallpaper = profile[config.USER_NAME]['wallpaper'],
            colorscheme = profile[config.USER_NAME]['colorscheme']
        )

@app.route('/get_more_posts', methods=['GET', 'POST'])
def get_more_posts():

    if request.method == 'POST':
        posts = scrapie.get_girls_posts_info(config.URL_ID + request.form.get('id'))

    else:
        posts = scrapie.get_girls_posts_info(config.URL_PAGE + "2")

    return render_template(
        'more_posts.html',
        posts=posts
    )








