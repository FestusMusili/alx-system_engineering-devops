#!/usr/bin/python3
"""
Converts to-do list details for a specified employee ID into JSON format.

This script retrieves information about the user and their to-do list items for a given
employee ID from the JSONPlaceholder API and saves them as a JSON file.
"""

import json
import requests
import sys

if __name__ == "__main__":
    # Get the employee ID from the command-line argument
    user_id = sys.argv[1]

    # Define the base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information based on the provided employee ID
    user_info = requests.get(base_url + "users/{}".format(user_id)).json()
    username = user_info.get("username")

    # Fetch the to-do list for the employee using the provided employee ID
    todos = requests.get(base_url + "todos", params={"userId": user_id}).json()

    # Create a dictionary containing the user and their to-do list information
    data_to_export = {
        user_id: [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username
            }
            for todo in todos
        ]
    }

    # Save the data as a JSON file with the employee ID as the filename
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)
