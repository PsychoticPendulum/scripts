#! /usr/bin/env python3

import requests
import os

def clone_all_repositories(token, username):
    api_url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(api_url)

    if response.status_code == 200:
        repos = response.json()
        for repo in repos:
            repo_name = repo["name"]
            repo_url = repo["clone_url"]
            os.system(f"git clone https://{token}@github.com/{username}/{repo_name}")
            print(f"Cloned repository {repo_name}")
    else:
        print(f"Failed to fetch repositories for {username}. Status code: {response.status_code}")

if __name__ == "__main__":
    github_username = "psychoticpendulum"
    clone_all_repositories(input("Enter token: "), github_username)
