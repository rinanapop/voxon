import yaml

def create_new_user(user_name):

    with open('profile.yml', 'w') as yf:
        yaml.dump({
            user_name: {
                "wallpaper": "genshin-impact.jpg",
                "colorscheme": "dark"
                }
            
        }, yf)

create_new_user("rinanapop")
