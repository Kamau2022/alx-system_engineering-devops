#!/usr/bin/python3
"""Python script to export data in the json format.
"""
import json
import requests
import sys
if __name__ == "__main__":
    p = sys.argv[1]
    url_2 = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(p)
    url_1 = 'https://jsonplaceholder.typicode.com/users/{}'.format(p)
    k = requests.get(url_1)
    name = k.json()['username']
    response = requests.get(url_2)
    user_id = p
    data = {user_id: []}
    for x in response.json():
        newdata = {"task": x['title'], "completed": x['completed'],
                   "username": name}
        data[user_id].append(newdata)
    with open("{}.json".format(p), "w") as f:
        json.dump(data, f)
