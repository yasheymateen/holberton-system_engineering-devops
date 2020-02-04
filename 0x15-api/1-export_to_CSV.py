#!/usr/bin/env python3
""" extend python script to export data in the csv format """

import json
import sys
import csv
import requests

if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit(1)

    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/todos?userId=' + user_id
    r = requests.get(url)
    file_name = user_id + ".csv"
    n = requests.get('https://jsonplaceholder.typicode.com/users/' + user_id)
    name = n.json().get('username')

    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        for user in r.json():
            writer.writerow([user_id, name, str(user.get('completed')),
                             user.get('title')])
