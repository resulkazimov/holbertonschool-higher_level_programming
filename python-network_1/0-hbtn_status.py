#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status using urllib.
"""
import urllib.request


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    req = urllib.request.Request(url)
    # Adding the mandatory header for firewall bypass
    req.add_header('cfclearance', 'true')

    with urllib.request.urlopen(req) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
