#!/usr/bin/python3
"""
This script Write a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""


import sys
import requests


def get_github_id(username, token):
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, token))

    if response.status_code == 200:
        user_data = response.json()
        return (user_data['id'])
    else:
        return None


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]

    user_id = get_github_id(username, password)
    print(user_id)
