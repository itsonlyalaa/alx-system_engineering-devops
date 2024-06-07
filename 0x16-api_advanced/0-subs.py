#!/usr/bin/python3
"""API subs module"""

import requests


def number_of_subscribers(subreddit):
    """a function that queries the Reddit API
    and returns the number of subscribers
    """
    information = requests.get("https://www.reddit.com/r/{}/about.json"
                 .format(subreddit),
                headers={"User-Agent": "Custom-User-Agent"},
                allow_redirects=False)
    if information.status_code >= 300:
        return 0
    return information.json().get("data").get("subscribers")
