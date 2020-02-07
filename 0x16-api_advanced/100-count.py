#!/usr/bin/python3
"""Queries the Reddit API recursively, parses the title of all hot articles,
and prints a sorted count of given keywords (case-insensitive, delimited by
spaces. Javascript should count as javascript, but java should not).
"""
import requests


def count_words(subreddit, word_list, word_dict={}, name=None, first=True):
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) '
               'AppleWebKit/537.36 (KHTML, like Gecko) '
               'Chrome/71.0.3578.98 Safari/537.36',
               'Content-Type': 'application/json'}
    if name:
        url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
            subreddit, name)
    else:
        url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if not word_dict:
        word_dict = {word: 0 for word in word_list}
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code != requests.codes.ok:
        return None
    hot_posts = r.json().get('data').get('children')
    for post in hot_posts:
        if post == hot_posts[-1]:
            title_words = post.get('data').get('title').lower().split()
            for word in title_words:
                if word in word_dict:
                    word_dict[word] += 1
            name = post.get('data').get('name')
            count_words(subreddit, word_list, word_dict, name, False)
        else:
            title_words = post.get('data').get('title').lower().split()
            for word in title_words:
                if word in word_dict:
                    word_dict[word] += 1
    if first:
        sorted_by_value = sorted(word_dict.items(), key=lambda kv: kv[1],
                                 reverse=True)
        for k, v in sorted_by_value:
            if v != 0:
                print("{}: {}".format(k, v))
