#!/usr/bin/python3
"""
Returns information about employee TODO list progress
"""
from sys import argv
import requests
import csv

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    uname = user.get("username")
    todos = requests.get(url + "todos", params={"userId": argv[1]}).json()

    with open("{}.csv".format(argv[1]), "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for t in todos:
            writer.writerow(
                    [argv[1], uname, t.get("completed"), t.get("title")])
