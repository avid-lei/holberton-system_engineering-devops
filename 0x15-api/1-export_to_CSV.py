#!/usr/bin/python3
"""export in CSV format"""

if __name__ == '__main__':
    import csv
    import requests
    from sys import argv

    urlID = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                         format(argv[1]))

    jID = urlID.json()
    name = jID.get('username')

    urlTD = requests.get('https://jsonplaceholder.typicode.com/todos')
    jTD = urlTD.json()

    with open(argv[1] + ".csv", 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC,)

        for x in jTD:
            if str(x.get("userId")) == argv[1]:
                com = str(x.get('completed'))
                title = str(x.get('title'))
                writer.writerow([argv[1], name, com, title])
