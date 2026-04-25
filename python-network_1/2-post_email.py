#!/usr/bin/python3
"""
Sends a POST request to a given URL with an email as a parameter.
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values).encode('ascii')
    req = urllib.request.Request(url, data)
    req.add_header('cfclearance', 'true')

    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
