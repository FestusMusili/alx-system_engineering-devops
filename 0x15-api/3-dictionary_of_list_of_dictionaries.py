#!/usr/bin/python3
"""
Exports to-do list information of all employees to JSON format.

This script retrieves user details and their respective \
to-do lists for all employees
"""

import json
import requests


def fetch_user_data():
    """Retrieves user details and to-do lists for all employees."""
    # Base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Retrieve the list of all users (employees)
    users = requests.get(base_url + "users").json()

    # Create a dictionary to store the to-do list information for all employees
    data_to_export = {}

    # Iterate through each user and fetch their to-do list
    for user in users:
        user_id = user["id"]
        user_url = base_url + f"todos?userId={user_id}"
        todo_list = requests.get(user_url).json()

        # Store the to-do list information in the dictionary
        data_to_export[user_id] = [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username"),
            }
            for todo in todo_list
        ]

    return data_to_export


if __name__ == "__main__":
    # Fetch user data for all employees
    data_to_export = fetch_user_data()

    # Write the data to a JSON file
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
