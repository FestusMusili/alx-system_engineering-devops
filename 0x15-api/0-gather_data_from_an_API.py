#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress.

You must use urllib or requests module
The script must accept an integer as a parameter, which is the employee ID
"""
# Importing the requests module for making HTTP requests
import requests
# Importing the sys module for accessing command line arguments
import sys

if __name__ == "__main__":
    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Retrieving the employee information using the provided employee ID
    employee_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(employee_id)).json()

    # Retrieving the to-do list for the employee using the provided employee ID
    params = {"userId": employee_id}
    todos = requests.get(url + "todos", params).json()

    # Filtering completed tasks and counting them
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    # Displaying the employee's name and the number of completed tasks
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    # Displaying the titles of completed tasks with indentation
    [print("\t {}".format(complete)) for complete in completed]
