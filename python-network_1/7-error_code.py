#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the response.
Handles HTTP status codes greater than or equal to 400.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    headers = {'cfclearance': 'true'}
    response = requests.get(url, headers=headers)

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
