#!/usr/bin/python3
"""
This script t takes 2 arguments in order to solve this challenge.
"""


import sys
import requests


def get_commits(repo, owner):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:
            sha = commit['sha']
            author = commit['commit']['author']['name']
            print(f"{sha}: {author}")
    else:
        print(f"Failed to fetch commits: {response.status_code}")


if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    get_commits(repo, owner)
