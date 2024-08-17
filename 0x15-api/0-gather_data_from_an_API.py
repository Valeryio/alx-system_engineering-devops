#!/usr/bin/python3

"""Get informations of an employee from an api
It shows some informations from the employes
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
        employe_name = employe_response.json().get("name")

    if response.status_code == 200:
        task_list = response.json()

        completed_tasks = []
        uncompleted_tasks = []

        for task in task_list:
            if task.get("completed"):
                completed_tasks.append(task)
            else:
                uncompleted_tasks.append(task)

        print(f"Employee {employe_name} is done with tasks\
({len(completed_tasks)}/{len(task_list)}):")

        for task in completed_tasks:
            print(f"\t {task.get('title')}")
