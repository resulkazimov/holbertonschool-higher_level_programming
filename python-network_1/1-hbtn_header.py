#!/usr/bin/python3
"""
Sends a request to a URL and displays the X-Request-Id header value.
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    req.add_header('cfclearance', 'true')

    with urllib.request.urlopen(req) as response:
        print(response.headers.get('X-Request-Id'))
