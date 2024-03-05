#!/usr/bin/python3
"""
Module that defines the recurse function
"""


def recurse(subreddit, hot_list=[], after="", count=0):
    """Recursive function"""
    import requests

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    params = {"after": after, "count": count, "limit": 100}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None

    data = response.json().get("data")
    after = data.get("after")
    count = data.get("dist")

    for child in data.get("children"):
        hot_list.append(child.get("data").get("title"))

    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after, count)
