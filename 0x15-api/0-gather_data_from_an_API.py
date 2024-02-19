#!/usr/bin/python3
"""
Returns information about employee TODO list progress
"""
import requests
import sys
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    finished = [t.get('title') for t in todos if t.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):".format(
          employee.get("name"), len(finished), len(todos)))
    [print("\t {}".format(c)) for c in finished]
