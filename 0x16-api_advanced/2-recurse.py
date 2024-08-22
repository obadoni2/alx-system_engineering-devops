#!/urs/bin/python3
"""a recursive function that queries the AP1 and return a list
containing the title of all hot articles for a given subreddit
"""
import requests

def recurse(subreddit, hot_list=[], after="", count=0):
    """Return a list of title of all hot posts on a given subreddit."""
    sub_info = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params ={"count": count, "after": after},
                            headers ={"user-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code >= 400:
        return None
    hot_1 = hot_list +[child.get("data").get("title")
                       for child in sub_info.json()
                       .get("data")
                       .get("children")]
    info =sub_info.json()
    if not info.get("data").get("after"):
        return hot_1
    return recurse(subreddit, hot_1, info.get("count"),
                   info.get("data").get("after"))
    
    