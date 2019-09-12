# app.py

import sys

import requests


def get_stars(owner, repo):
    url = f'https://api.github.com/repos/{owner}/{repo}'
    stars = requests.get(url).json()['stargazers_count']
    return stars


if __name__ == '__main__':
    print(get_stars(sys.argv[1], sys.argv[2]))
