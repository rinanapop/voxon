import os
import yaml
import config

def update(target, new_value):
    
    with open(config.PROFILE, 'r+') as yf:
        conf_file = yaml.safe_load(yf)
        conf_file[config.USER_NAME][target] = new_value

    with open(config.PROFILE, 'w') as yf:
        yf.write(str(conf_file))
