#!/usr/bin/python3
"""This script sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response.
"""


import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        x_id = response.getheader('X-Request-Id')
        print(x_id)
