#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request to the passed
URLwith the email as a parameter, and displays the body of
the response (decoded in utf-8)
"""


import urllib.request
import sys
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    values = {'email': email}

    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
    
    print(html)
