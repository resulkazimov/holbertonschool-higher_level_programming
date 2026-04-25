#!/usr/bin/python3
"""
Sends a POST request to a URL with an email as a parameter using requests.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    payload = {'email': sys.argv[2]}
    headers = {'cfclearance': 'true'}
    response = requests.post(url, data=payload, headers=headers)
    print(response.text)
