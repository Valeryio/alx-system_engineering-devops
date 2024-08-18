#!/usr/bin/python3

""" THis module export the task done by the
    module 1
"""

import requests
import sys


if __name__ == "__main__":

    employe_id = sys.argv[1]
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos\
            ".format(employe_id)
    employe_url = f"https://jsonplaceholder.typicode.com/users/{employe_id}"

    response = requests.get(todo_url)
    employe_response = requests.get(employe_url)

    if employe_response.status_code == 200:
        employe_name = employe_response.json().get("username")

    if response.status_code == 200:
        task_list = response.json()

        completed_tasks = []
        uncompleted_tasks = []

    with open(f'{employe_id}.csv', 'w') as csvfile:
        for task in task_list:
            print(task)
            csvfile.write("\"{}\",\"{}\",\"{}\",\"{}\"\n".format(
                task["userId"], employe_name,
                task["completed"], task["title"]))
