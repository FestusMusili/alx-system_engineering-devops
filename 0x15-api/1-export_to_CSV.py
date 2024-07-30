#!/usr/bin/python3
"""This script exports the to-do list information
for a specified employee ID into CSV format."""

import csv
import requests
import sys

if __name__ == "__main__":
    # Extracting the user ID from the command-line arguments
    user_id = sys.argv[1]

    # Defining the base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetching user data from the API and \
    converting the response to JSON format
    user_data = requests.get(base_url + "users/{}".format(user_id)).json()

    # Retrieving the username from the user data
    username = user_data.get("username")

    # Fetching the to-do list items associated with the specified user ID
    # and converting the response to JSON format
    todo_items = requests.get(base_url + "todos",
                              params={"userId": user_id}).json()

    # Using list comprehension to iterate through the to-do list items
    # and writing each item's details (user ID, username, completion status,
    # and title) as a row in the CSV file
    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [csv_writer.writerow(
            [user_id, username, todo.get("completed"), todo.get("title")]
         ) for todo in todo_items]
