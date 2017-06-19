import requests
import json
import datetime as dt
import argparse
import pytz

FORMAT_TIME = '%H:%M'
URL_TEMPLATE = 'https://devman.org/api/challenges/solution_attempts/'
DEFAULT_TIME = '06:00'
PAGES = 10


def load_attempts():
    for page in range(1, PAGES):
        response = requests.get(URL_TEMPLATE,
                                params={'page': page})
        content_massive = response.json()['records']
        for content in content_massive:
            if content['timestamp']:
                yield content


def get_midnighters(content, end_time):
    timezone = pytz.timezone(content['timezone'])
    delivery_time = dt.datetime.fromtimestamp(content['timestamp'],
                                              timezone).time()
    if delivery_time < end_time:
        yield {'user': content['username'], 'time': delivery_time}


def print_midnighters(content, end_time):
    for user in get_midnighters(content, end_time):
        print('User "{user}" sent work at {time}'.format(**user))


def create_parser_for_user_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--time',
                        help="Up to what time displayed from 00.00 o'clock",
                        default=DEFAULT_TIME,
                        type=lambda t:
                            dt.datetime.strptime(t, FORMAT_TIME).time())
    namespace = parser.parse_args()
    return namespace


if __name__ == '__main__':
    namespace = create_parser_for_user_arguments()
    end_time = namespace.time
    for content in load_attempts():
        print_midnighters(content, end_time)
