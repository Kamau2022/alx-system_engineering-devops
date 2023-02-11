#!/usr/bin/python3
"""Python script to export data in the json format.
"""
import json
import requests
import sys
if __name__ == "__main__":
    url_2 = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url_2)
    user_id = 1
    data = {user_id: []}
    for x in response.json():
        Id = x.get('userId')
        k = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                         .format(Id))
        username = k.json().get('username')
        newdata = {"username": username, "task": x['title'],
                   "completed": x['completed']}
        data[user_id].append(newdata)
    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)
