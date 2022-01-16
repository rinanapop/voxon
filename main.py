from voxon import app
from flask import render_template

@app.route('/')
def index():
    data = [
        {'title': 'something',
        'price': 'something',
        'day': 'something'},

        {'title': 'anything',
        'price': 'anything',
        'day': 'anything'}
    ]

    return render_template(
        'base.html',
        data = data
    )
