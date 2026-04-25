#!/usr/bin/python3
"""
Sends a request to a URL and displays the value of the X-Request-Id.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    headers = {'cfclearance': 'true'}
    response = requests.get(url, headers=headers)
    print(response.headers.get('X-Request-Id'))
