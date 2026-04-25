#!/usr/bin/python3
"""
Uses GitHub API to display a user's id using Basic Authentication.
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    headers = {'cfclearance': 'true'}

    response = requests.get(url, auth=(username, password), headers=headers)
    try:
        json_data = response.json()
        print(json_data.get('id'))
    except ValueError:
        print("None")
