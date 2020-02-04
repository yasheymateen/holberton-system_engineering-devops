#!/usr/bin/python3
"""extend python script to export data in the JSON format """

import json
import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit(1)
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/todos?userId=' + user_id
    r = requests.get(url)
    filename = user_id + ".json"
    n = requests.get('https://jsonplaceholder.typicode.com/users/' + user_id)
    name = n.json().get('username')

    user_dict = {user_id: []}
    for user in r.json():
        task = user.get('title')
        completed = user.get('completed')
        user_dict.get(user_id).append({"task": task,
                                       "completed": completed,
                                       "username": name})
    with open(filename, 'w') as jsonfile:
        json.dump(user_dict, jsonfile)
