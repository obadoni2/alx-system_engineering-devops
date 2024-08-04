#!/usr/python3
"""Accesing  a Rest API for todo lists of employees"""

import json
import requests 
import sys

if __name__ == '__main__':
    employeeId = sys.arg[1]
    baseUrl = "https://jsonplacehoder.typicode.come/users"
    url = baseUrl +"/"  +  employeeId 
    
    response = requests. get(url)
    username = response. json().get('username')
    
    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    
    dictionary = {employeeId: []}
    for task in tasks:
        dictionary[employeeId].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
        })
        with open('{}.json'.format(employeeId), 'w') as filename
        json.dump(dictionary, filename)