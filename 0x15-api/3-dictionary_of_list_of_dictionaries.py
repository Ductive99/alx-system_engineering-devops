#!/usr/bin/python3
"""
Saves information on all employees in JSON
"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as f:
        json.dump({
            u.get("id"): [{
                "task": todos.get("title"),
                "completed": todos.get("completed"),
                "username": u.get("username")
            } for todos in requests.get(url + "todos",
                                        params={"userId": u.get("id")}).json()]
            for u in users}, f, indent=2)
