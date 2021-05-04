#!/usr/bin/python3
""" Using what you did in the task #0, extend your Python script
    to export data in the JSON format """

import json
import requests as r
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    x = r.get('https://jsonplaceholder.typicode.com/users/{}/todos'
              .format(user))
    y = r.get('https://jsonplaceholder.typicode.com/users/{}'.format(user))
    json_obj_todo = x.json()
    json_ob_user = y.json()
    data = {}
    username = json_ob_user.get('username')
    tasks_info = []
    for task in json_obj_todo:
        dic = {}
        dic['task'] = task.get('title')
        dic['completed'] = task.get('completed')
        dic['username'] = username
        tasks_info.append(dic)
    data[user] = tasks_info

    with open("{}.json".format(user), "w")as f:
        json.dump(data, f)
