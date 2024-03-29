#!/usr/bin/python3
import requests

"""
Function that queries Reddit's API for total
number of subscribers of a subreddit
"""

def number_of_subscribers(subreddit):
    """
    Function that queries Reddit's API for total
    number of subscribers of a subreddit
    """
    url = 'https://www.reddit.com/r/{}/about.json'\
            .format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; \
            Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    response = response.json().get('data').get('subscribers')
    return response
