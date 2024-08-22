#!/usr/bin/python3
"""
a recursive function that quaries the  Reddit API, parses the title of all
hot articles, and prints a sorted count of given keyword

"""
import requests

def count_words(subreddit, word_list, instance={}, after="", count=0):
    """
    Return  a list containing the title of all hot article for a 
    given subreddit.if no result are found for the given subreddit
    the function return
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers= {
        "User-Agent": "linux:0x16.api.advance:V1.0.0 (by/u/bdov_)"
        
    }
    params={
        "after":after,
        "count": count,
        "limit":100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    try:
        results = response.json()
        if response.status_code ==404:
            raise Exception
    except Exception:
        print("")
        return
    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")
    for ct in results.get("children"):
        title = ct.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times =len([tm for tm in title if tm == word.lower()])
                if instance.get(word) is None:
                    instances[words] = times
                else:
                    instance[word] +=times
        if after is None:
            if len(instances) == 0:
                print("")
                return
            instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
            [print("{}: {}".format(k, v)) for k, v in instances]
        else:
            count_words(subreddit, word_list, instance, after, count)
    
    