#!/usr/bin/python3
"""
Returns information about employee TODO list progress
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    uname = user.get("username")
    todos = requests.get(url + "todos", params={"userId": argv[1]}).json()

    with open("{}.json".format(argv[1]), "w") as f:
        json.dump({argv[1]: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": uname
            } for t in todos]}, f, indent=2)
