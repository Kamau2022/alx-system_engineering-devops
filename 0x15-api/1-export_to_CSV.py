#!/usr/bin/python3
"""Python script to export data in the CSV format.
"""
import csv
import json
import requests
import sys
if __name__ == "__main__":
    count = 0
    p = sys.argv[1]
    url_2 = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(p)
    url_1 = 'https://jsonplaceholder.typicode.com/users/{}'.format(p)
    k = requests.get(url_1)
    name = k.json()['username']
    response = requests.get(url_2)
    with open('{}.csv'.format(p), 'w', newline='') as file:
        for data in response.json():
            d = data['userId'], name, data['completed'], data['title']
            writer = csv.writer(file,   delimiter=',', quoting=csv.QUOTE_ALL)
            writer.writerow(d)
