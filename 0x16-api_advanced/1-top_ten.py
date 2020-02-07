#!/usr/bin/python3
""" queries reddit api and prints titles of first 10 hot posts """
import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
               'AppleWebKit/537.36 (KHTML, like Gecko) '
               'Chrome/71.0.3578.98 Safari/537.36',
               'Content-Type': 'application/json'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    r = requests.get(url, headers=headers)
    if r.status_code != requests.codes.ok:
        print('None')
        return 0
    hot_posts = r.json()
    if len(hot_posts.get('data').get('children')) == 0:
        print('None')
        return 0
    for i in range(10):
        post = hot_posts.get('data').get('children')[i]
        print(post.get('data').get('title'))
