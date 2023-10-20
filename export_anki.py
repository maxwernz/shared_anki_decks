#!/usr/local/bin/python3
import requests
import os
import sys
from git_util import git_pull, git_push

# Anki Connect API URL
anki_connect_url = "http://localhost:8765"

def export_deck(deck_name):

    cwd = os.getcwd() + '/'
    data = {
        "action": "exportPackage",
        "params": {
            "deck": deck_name,
            "path": f"{cwd}{deck_name}.apkg"
        }
    }

    try:
        response = requests.post(anki_connect_url, json=data)
        print(response.json())
        response_data = response.json()

        if response_data:
            print(f"Exported deck {deck_name} successfully.")
        else:
            print(f"Failed to export deck")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    args = sys.argv[1:]
    print(args)
    git_pull()
    for arg in args:
        export_deck(arg)

    apkg_files = [file for file in os.listdir(os.getcwd()) if file.endswith(".apkg")]
    git_push(apkg_files)
