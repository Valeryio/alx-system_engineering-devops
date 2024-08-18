#!/usr/bin/python3

"""
    THis module export data to json
"""

import json
import requests


if __name__ == "__main__":

    # requests to get the data from the jsonplaceholder... API
    all_employees = requests.get("https://jsonplaceholder.typicode.com/users")
    all_employees = all_employees.json()

    json_obj = {}

    for employee in all_employees:
        # print(employee)
        employee_tasks = requests.get("https://jsonplaceholder.typicode.com/\
users/{}/todos".format(employee["id"]))

        all_tasks = employee_tasks.json()
        tasks_list = []

        # create the appropriate python object
        for i in range(len(all_tasks)):
            new_dict = {}
            new_dict["task"] = all_tasks[i]["title"]
            new_dict["completed"] = all_tasks[i]["completed"]
            new_dict["username"] = employee.get("username")
            tasks_list.append(new_dict)

        json_obj[employee["id"]] = tasks_list

    # convert the python object to a json file
    json_obj = json.dumps(json_obj)

    # write the json object into the file
    filename = "todo_all_employees.json"
    with open(filename, "w") as file:
        file.write(json_obj)
