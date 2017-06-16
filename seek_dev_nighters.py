import requests
import json
from datetime import datetime


def load_attempts():
    pages = 10
    for page in range(3, pages):
        api_url = 'https://devman.org/api/challenges/solution_attempts/?page={}'.format(page)
        response = requests.get(api_url)
        json_obj = response.content
        content_list = json.loads(json_obj)
        yield content_list


def get_users_info(content_list):
    #for info in content_list['records']:
    #    return {
    #        'username': info['username'],
    #        'timestamp': info['timestamp'],
    #        'timezone':  info['timezone']
    #    }
    users_info_list=[{'username': info['username'], 'timestamp': info['timestamp'], 'timezone':  info['timezone']} for info in content_list['records']]
    return users_info_list

def get_midnighters(timestamp):
    for users in timestamp:
        #print(users)
        delivery_time = datetime.fromtimestamp(users['timestamp']).time()
        print(delivery_time)
        #return delivery_time


if __name__ == '__main__':
    for content_list in load_attempts():
        content=get_users_info(content_list)
        get_midnighters(content)
