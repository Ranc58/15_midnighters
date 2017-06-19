import requests
import json
import datetime as dt
from itertools import product

def load_attempts():
    pages = 10
    for page in range(3, pages):
        api_url = 'https://devman.org/api/challenges/solution_attempts/?page={}'.format(page)
        response = requests.get(api_url)
        json_obj = response.content
        content_list = json.loads(json_obj)
        yield content_list


def get_users_info(content_list):
    users_info_list=[{'username': info['username'],
                      'timestamp': info['timestamp'],
                      'timezone':  info['timezone']}
                     for info in content_list['records']]
    return users_info_list


def get_midnighters(users_info_list):
    for user in users_info_list:
        delivery_time = dt.datetime.fromtimestamp(user['timestamp']).time()
        if delivery_time < dt.time(6, 0):
            yield {'user':user['username'],'time':delivery_time}

def print()

if __name__ == '__main__':
    for content_list in load_attempts():
        for user in get_midnighters(get_users_info(content_list)):
            print('User {user} sent work at {time}'.format(**user))
