import requests
import datetime as dt
import argparse
import pytz

FORMAT_TIME = '%H:%M'
URL_TEMPLATE = 'https://devman.org/api/challenges/solution_attempts/'
DEFAULT_TIME = '06:00'


class Midnighter:
    def __init__(self, content, end_time):
        self.content = content
        self.end_time = end_time

    def get_midnighters(self):
        timezone = pytz.timezone(self.content['timezone'])
        delivery_time = dt.datetime.fromtimestamp(self.content['timestamp'],
                                                  timezone).time()
        if delivery_time < self.end_time:
            yield {'user': self.content['username'], 'time': delivery_time}

    def print_midnighters(self):
        for user in Midnighter.get_midnighters(self):
            print('User "{user}" sent work at {time}'.format(**user))


def load_attempts():
    current_page = 1
    pages_for_parse = 1
    while current_page <= pages_for_parse:
        response = requests.get(URL_TEMPLATE, params={"page": current_page}).json()
        pages_for_parse = response["number_of_pages"]
        current_page += 1
        for user_info in response["records"]:
            if user_info['timestamp']:
                yield user_info



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
        Midnighter(content, end_time).print_midnighters()
