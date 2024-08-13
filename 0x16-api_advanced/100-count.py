#!/usr/bin/python3
"""
Queries the Reddit API recursively and prints a sorted count of given keywords
"""

import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
    Recursively queries the Reddit API

    Args:
        subreddit (str): The name of the subreddit to search for.
        word_list (list): A list of keywords to count occurrences of.
        after (str): The value of the 'after' parameter for pagination
        counts (dict): A dictionary to store keyword counts

    Returns:
        None
    """
    # Base case: if subreddit is invalid, print nothing
    if subreddit is None:
        return

    # Construct the URL for fetching hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    if after:
        url += f"&after={after}"

    headers = {'User-Agent': 'MyRedditBot/1.0'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return

    data = response.json()
    posts = data['data']['children']
    for post in posts:
        title = post['data']['title'].lower()
        for word in word_list:
            if word.lower() in title.split():
                counts[word.lower()] = counts.get(word.lower(), 0) + 1

    if data['data']['after'] is not None:
        count_words(subreddit, word_list, data['data']['after'], counts)

    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")
