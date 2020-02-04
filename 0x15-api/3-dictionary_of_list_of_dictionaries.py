#!/usr/bin/python3
"""extend python script to export data in the JSON format with all tasks """

import json
import requests
import sys

if __name__ == '__main__':
    num_users = len(requests.get(
        'https://jsonplaceholder.typicode.com/users').json())
    filename = 'todo_all_employees.json'

    all_employees = {}

    for user_id in range(1, num_users + 1):
        all_employees[str(user_id)] = []
        name = requests.get('https://jsonplaceholder.typicode.com/users/' +
                            str(user_id))
        name = name.json().get('username')

        url = 'https://jsonplaceholder.typicode.com/todos?userId='
        url += str(user_id)
        r = requests.get(url)
        for user in r.json():
            task = user.get('title')
            completed = user.get('completed')
            all_employees.get(str(user_id)).append({"task": task,
                                                    "completed": completed,
                                                    "username": name})
    with open(filename, 'w') as jsonfile:
        json.dump(all_employees, jsonfile)
