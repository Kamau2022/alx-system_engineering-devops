#!/usr/bin/python3
"""a script that uses a REST API for a given employee ID
"""
import json
import requests
import sys

count = 0
p = sys.argv[1]
url_1 = 'https://jsonplaceholder.typicode.com/users/{}'.format(p)
url_2 = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(p)
k = requests.get(url_1)
name = k.json()['name']
response = requests.get(url_2)
length = len(response.json())
for data in response.json():
    if data['completed'] is True:
        k = data['title']
        count += 1
print('Employee {} is done with tasks({}/{}):'.format(name, count, length))
for data in response.json():
    if data['completed'] is True:
        print('\t', '', data['title'])
