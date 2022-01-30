from voxon import app
from flask import render_template
import sqlite3
from . import scrapie

URL = "https://skypech.com"

@app.route('/')
def index():

    posts = scrapie.get_girls_posts_info(URL)

    intro1 = [
        "俺はやることがあるから、あとから合流するわ。俺のパソコン使っていいから、昨日話したとおりにやっておいてほしい。",
        "あ、余計なところは見なくていいのでwww",
        "やっとあともう少しってところまで来たんだし、さっさと終わらせようぜ~",
        'ユーザーネームは"miy@uch1"',
        "パスワードはラミ・マレックの誕生日をYYYYMMDDにしてあるからよろしく。じゃあ。"
    ]
    intro2 = [
        "たまには息を抜いてリラックスしろよな",
        "河川敷で待ってるからさ",
        "ごめんだけど、コーヒー買ってきてくれる？"
    ]

    return render_template(
        'base.html',
        message1 = intro1,
        message2 = intro2,
        posts=posts
    )
