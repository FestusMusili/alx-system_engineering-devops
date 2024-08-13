#!/usr/bin/python3
"""
Queries the Reddit API and print the titles of the first 10 post
"""


import requests


def top_ten(subreddit):
    """
    Queries the Reddit API
    Args: subreddit (str): name of the subreddit to search for
    Returns: None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    response = requests.get(url, headers=headers)
    data = response.json()
    posts = data['data']['children']
    for post in posts:
        print(post['data']['title'])
