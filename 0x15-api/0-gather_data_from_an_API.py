#!/usr/bin/env python3
""" using rest API, return information about a given employee id's progress"""

import json
import sys
import requests

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Error: Integer parameter for Employee ID required.')
        exit(1)

    name = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]
    name = requests.get(name).json().get('name')
    url = 'https://jsonplaceholder.typicode.com/todos?userId=' + sys.argv[1]
    r = requests.get(url)

    total_tasks = 0
    number_done = 0
    task_progress = []
    for user in r.json():
        total_tasks += 1
        if user.get('completed') is True:
            task_progress.append(user.get('title'))
            number_done += 1
    first_line = 'Employee {} is done with tasks({}/{})'.format(name,
                                                                number_done,
                                                                total_tasks)
    print(first_line)
    for task in task_progress:
        print('\t', task)
