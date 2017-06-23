import requests
import datetime as dt
import argparse
import pytz

FORMAT_TIME = '%H:%M'
URL_TEMPLATE = 'https://devman.org/api/challenges/solution_attempts/'
DEFAULT_TIME = '06:00'


def load_attempts():
    get_full_info = requests.get(URL_TEMPLATE).json()
    pages_quantity = get_full_info['number_of_pages']
    first_page_info = get_full_info['records']
    for user_info in first_page_info:
        if user_info['timestamp']:
            yield user_info
    for page in range(2, pages_quantity):
        params = {'page': page}
        user_info_massive = requests.get(URL_TEMPLATE,
                                         params=params).json()
        for user_info in user_info_massive['records']:
            if user_info['timestamp']:
                yield user_info


def check_midnighter(user_info, end_time):
    timezone = pytz.timezone(user_info['timezone'])
    delivery_time = dt.datetime.fromtimestamp(user_info['timestamp'],
                                              timezone).time()
    if delivery_time < end_time:
        yield {'user': user_info['username'],
               'time': delivery_time.strftime(FORMAT_TIME)}


def print_midnighters(user_info, end_time):
    for user in check_midnighter(user_info, end_time):
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
    for user_info in load_attempts():
        print_midnighters(user_info, end_time)
