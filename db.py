import sqlite3
from . import scrapie

DATABASE = 'posts_info.db'
INSERT_SQL ='INSERT INTO posts VALUES(?,?,?,?,?,?,?)' 

def create_posts_table():
    con = sqlite3.connect(DATABASE)
    con.execute('CREATE TABLE IF NOT EXISTS posts \
                (icon, name, skype_id, post_id, title, message, date)')
    con.close()

def reload_new_posts():
    con = sqlite3.connect(DATABASE)
    posts = scrapie.get_girls_posts_info()
    
    for post in posts:
        con.execute(INSERT_SQL,
                    [post['icon'], post['name'], post['skype_id'], post['post_id'], \
                    post['title'], post['message'], post['date']])
        con.commit()
    con.close()
