#!/usr/bin/python3
"""Prototype: def number_of_subscribers(subreddit)
   If not a valid subreddit, return 0.
   NOTE: Invalid subreddits may return a redirect to search results.\
   Ensure that you are not following redirects."""
import requests


def number_of_subscribers(subreddit):
    """def"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    if response.status_code == 200:
        return(response.json().get('data').get('subscribers'))
    return 0
