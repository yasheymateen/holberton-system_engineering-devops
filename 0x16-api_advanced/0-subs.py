#!/usr/bin/python3
""" Queries reddit api and returns number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ function that makes http request to reddit api to return subs"""
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
               'AppleWebKit/537.36 (KHTML, like Gecko) '
               'Chrome/71.0.3578.98 Safari/537.36',
               'Content-Type': 'application/json'}
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    r = requests.get(url, headers=headers)
    if r.status_code != requests.codes.ok:
        return 0
    else:
        response_data = r.json()
        return response_data.get('data').get('subscribers')
