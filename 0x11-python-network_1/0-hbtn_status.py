#!/usr/bin/python3
"""This script  fetches https://alx-intranet.hbtn.io/status"""


import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read
