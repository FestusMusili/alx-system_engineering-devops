#!/usr/bin/python3
"""
Queries the Reddit API recursively
"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    Recursively queries the Reddit API for hot topics.

    Args:
        subreddit (str): The name of the subreddit to search for.
        hot_list (list): A list containing the titles of hot articles

    Returns:
        list or None: A list containing the titles of hot topics
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"

    headers = {'User-Agent': 'MyRedditBot/1.0'}

    response = requests.get(url, headers=headers)

    data = response.json()
    posts = data['data']['children']
    for post in posts:
        hot_list.append(post['data']['title'])

    if data['data']['after'] is not None:
        return recurse(subreddit, hot_list=hot_list)

    return hot_list
