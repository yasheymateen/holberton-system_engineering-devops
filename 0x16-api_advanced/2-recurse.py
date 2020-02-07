#!/usr/bin/python3
""" recursive func that queries reddit api and returns list
containing titles of all hot articles for given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], name=None):
    """"Queries the Reddit API and returns a list containing the titles of all
    hot articles for a given subreddit. Else None.
    """
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
               'AppleWebKit/537.36 (KHTML, like Gecko) '
               'Chrome/71.0.3578.98 Safari/537.36',
               'Content-Type': 'application/json'}
    if name:
        url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
            subreddit, name)
    else:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    r = requests.get(url, headers=headers)
    if r.status_code != requests.codes.ok:
        return None
    hot_posts = r.json().get('data').get('children')
    for post in hot_posts:
        if post == hot_posts[-1]:
            hot_list.append(post.get('data').get('title'))
            name = post.get('data').get('name')
            recurse(subreddit, hot_list, name)
        else:
            hot_list.append(post.get('data').get('title'))
    return hot_list
