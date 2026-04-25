#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the response.
Handles HTTP errors and prints the error code.
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    req.add_header('cfclearance', 'true')

    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
