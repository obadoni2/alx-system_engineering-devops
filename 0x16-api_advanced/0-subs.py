#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""
from requests import  get

def number_of_subscribers(subreddit):
    """
    function that quaries the reddit Api and returnse  the number of subscribers
    (not active users, total subscribers) for a given subreddit


    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
        
    user_agent ={'User-agent': 'Google chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response =get(url, headers=user_agent)
    results = response.json()
    
    
    try:
        
        return results.get('data').get('subscriber')
    except Exception:
         return 0
     
        