import requests
import bs4

def get_girls_posts_info(URL):

    data_list = [] 
    resp = requests.get(URL)
    soup = bs4.BeautifulSoup(resp.text, "lxml")
    
    posts = soup.find_all(class_="gender2")

    for post in posts:
        data = {
            'icon': post.find('img').get('data-original'),
            'name': post.find('span').text.strip(),
            'skype_id': post.find('input').get('value'),
            'post_id': post.find('input').get('id'),
            'title': post.find(class_='post-title').text.strip(),
            'tags': [p.text.strip() for p in post.find_all(class_='tag')],
            'message': post.find(class_='post-message').text.strip(),
            'date': post.find(class_='post-updated').find('span').get('title')
        }

        data_list.append(data)

    return data_list

