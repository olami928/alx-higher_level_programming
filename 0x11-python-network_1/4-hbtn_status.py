#!/usr/bin/python3
"""
This script  fetches https://alx-intranet.hbtn.io/status
"""


import requests


if __name__ == "__main__":

    response = requests.get("https://alx-intranet.hbtn.io/status")
    html = response.text

    print("Body response:")
    print(f"\t- type: {type(html)}")
    print(f"\t- content: {html}")
