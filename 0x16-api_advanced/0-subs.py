#!/usr/bin/python3


def number_of_subscribers(subreddit):
    import requests
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh;' +
               ' Intel Mac OS X 10_10_1) AppleWebKit/537.36 ' +
               '(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    http = requests.get('https://www.reddit.com/r/{}/about.json'
                        .format(subreddit), headers=headers)
    if http.status_code == 404:
        return 0
    subscribers = http.json().get('data').get('subscribers')
    return subscribers
