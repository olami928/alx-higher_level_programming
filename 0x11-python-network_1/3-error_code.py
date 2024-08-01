#!/usr/bin/python3
"""
This is a script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""


import urllib.request
import sys
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]
    
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print(html)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
    except urllib.error.URLError as e:
        print(f"Error code: {e.reason}")
