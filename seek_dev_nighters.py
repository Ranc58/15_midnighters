import requests
import datetime as dt
import argparse
import pytz

FORMAT_TIME = '%H:%M'
URL_TEMPLATE = 'https://devman.org/api/challenges/solution_attempts/'
DEFAULT_TIME = '06:00'


def load_attempts():
    current_page = 1
    pages_for_parse = 1
    while current_page <= pages_for_parse:
        response = requests.get(URL_TEMPLATE,
                                params={"page": current_page}).json()
        pages_for_parse = response["number_of_pages"]
        current_page += 1
        for user_info in response["records"]:
            if user_info['timestamp']:
                yield user_info


def get_midnighters(end_time, content):
    timezone = pytz.timezone(content['timezone'])
    delivery_time = dt.datetime.fromtimestamp(content['timestamp'],
                                              timezone).time()
    if delivery_time < end_time:
        yield {'user': content['username'], 'time': delivery_time}


def print_midnighters(end_time, content):
    for user in get_midnighters(end_time, content):
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
        print_midnighters(end_time, content)
