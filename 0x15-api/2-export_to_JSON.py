#!/usr/bin/python3
"""export in json format"""

if __name__ == '__main__':
    import json
    import requests
    from sys import argv

    urlID = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                         format(argv[1]))

    jID = urlID.json()
    name = jID.get('username')

    urlTD = requests.get('https://jsonplaceholder.typicode.com/todos')
    jTD = urlTD.json()

    tasks = []

    for x in jTD:
        user = {}
        if str(x.get("userId")) == argv[1]:
                user['username'] = name
                user['task'] = str(x.get('title'))
                user['completed'] = str(x.get('completed'))
                tasks.append(user)

    users = {argv[1]: tasks}
    with open(argv[1] + ".json", "w") as f:
        f.write(json.dumps(users))
