from voxon import app
from flask import render_template
import sqlite3
from . import scrapie

URL = "https://skypech.com"

@app.route('/')
def index():


    posts = scrapie.get_girls_posts_info(URL)

    return render_template(
        'base.html',
        colorscheme="dark",
        posts=posts
    )
