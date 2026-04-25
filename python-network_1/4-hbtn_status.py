#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status using the requests package.
"""
import requests


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    headers = {'cfclearance': 'true'}
    response = requests.get(url, headers=headers)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
