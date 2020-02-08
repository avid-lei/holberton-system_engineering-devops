#!/usr/bin/python3

if __name__ == '__main__':
    import requests
    import sys

    user_id = sys.argv[1]
    name = requests.get('https://jsonplaceholder.typicode.com/users',
                        params={'id': user_id})
    name = name.json()[0].get('name')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos',
                         params={'userId': user_id})
    todos = todos.json()
    total_task = len(todos)

    todos_complete = [task for task in todos if task['completed']]
    completed_task = len(todos_complete)

    print("Employee {} is done with tasks({}/{}):".
          format(name, completed_task, total_task))
    for task in todos_complete:
        print("\t {}".format(task.get('title')))
