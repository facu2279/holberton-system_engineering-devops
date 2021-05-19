#!/usr/bin/python3
"""Write a function that queries the Reddit API and prints the titles of
   the first 10 hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """ def """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    if response.status_code == 200:
        hot_posts = response.json().get('data').get('children')
        for a in hot_posts:
            print(a.get('data').get('title'))
    else:
        print(None)
