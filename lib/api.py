import requests

BASE_URL = 'http://127.0.0.1:5000'


def get_form():
    return requests.get(BASE_URL)


def post_form(intervals, newInterval):
    return requests.post(f'{BASE_URL}/result', data={'intervals': intervals, 'newInterval': newInterval })


def get_page(url, headers=None):
    return requests.get(f'{BASE_URL}/{url}', headers=headers)


def post_data(url, data=None, headers=None):
    return requests.post(f'{BASE_URL}/{url}', headers=headers, data=data)
