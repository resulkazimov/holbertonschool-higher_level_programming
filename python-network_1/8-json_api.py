#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user with a letter.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': q}
    headers = {'cfclearance': 'true'}

    try:
        response = requests.post(url, data=payload, headers=headers)
        json_data = response.json()

        if not json_data:
            print("No result")
        else:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
    except ValueError:
        print("Not a valid JSON")
