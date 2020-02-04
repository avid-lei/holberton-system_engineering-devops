#!/usr/bin/python3
"""return info about todo life using RESTAPI"""

if __name__ == '__main__':
    from sys import argv
    import requests

    urlID = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                         format(argv[1]))

    jID = urlID.json()
    name = jID.get('name')

    urlTD = requests.get('https://jsonplaceholder.typicode.com/todos')
    jTD = urlTD.json()

    tt = 0
    td = 0

    for x in jTD:
        if str(x.get("userId")) == argv[1]:
            tt += 1
            if x.get('completed'):
                td += 1

    print('Employee {} is done with tasks({}/{}):'.format(name, td, tt))

    for x in jTD:
        if str(x.get("userId")) == argv[1]:
            if x.get('completed'):
                print('\t {}'.format(x.get('title')))
