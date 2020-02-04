#!/usr/bin/python3
"""export dict list of dict"""

if __name__ == '__main__':
    import json
    import requests

    urlID = requests.get('https://jsonplaceholder.typicode.com/users/')
    jID = urlID.json()

    users = {}
    for user in jID:
        tasks = []
        user_id = user.get('id')
        username = user.get('username')
        td = requests.get('https://jsonplaceholder.typicode.com/todos' +
                          '?userId={:}'.format(user_id))
        jtd = td.json()

        for x in jtd:
            user = {}
            user['username'] = username
            user['task'] = x.get('title')
            user['completed'] = x.get('completed')
            tasks.append(user)

        users[user_id] = tasks

    with open("todo_all_employees.json", "w") as f:
        json.dump(users, f)
