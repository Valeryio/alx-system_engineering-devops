#!/usr/bin/python3

"""
    THis module export data to json
"""

import json
import requests
import sys


if __name__ == "__main__":

    # requests to get the data from the jsonplaceholder... API
    employee_id = sys.argv[1]
    employee = requests.get("https://jsonplaceholder.typicode.com/users/{}\
".format(employee_id))
    employee_tasks = requests.get("https://jsonplaceholder.typicode.com/users/\
{}/todos".format(employee_id))

    all_tasks = employee_tasks.json()
    tasks_list = []
    json_obj = {}

    # create the appropriate python object
    for i in range(len(all_tasks)):
        new_dict = {}
        new_dict["task"] = all_tasks[i]["title"]
        new_dict["completed"] = all_tasks[i]["completed"]
        new_dict["username"] = employee.json().get("username")

        tasks_list.append(new_dict)

    # convert the python object to a json file
    json_obj[employee_id] = tasks_list
    json_obj = json.dumps(json_obj)

    # write the json object into the file
    filename = str(employee_id) + ".json"
    with open(filename, "w") as file:
        file.write(json_obj)
