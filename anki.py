#!/usr/local/bin/python3
import requests
import git
import os

def git_pull():
    g = git.cmd.Git(os.getcwd())
    g.pull()

# Anki Connect API URL
anki_connect_url = "http://localhost:8765"

def import_anki_deck(deck_path):
    # Prepare the request data
    data = {
        "action": "importPackage",
        "params": {
            "path": deck_path
        }
    }

    try:
        response = requests.post(anki_connect_url, json=data)
        print(response.json())
        response_data = response.json()

        if response_data:
            print(f"Imported deck from {deck_path} successfully.")
        else:
            print(f"Failed to import deck")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    git_pull()
    cwd = os.getcwd() + '/'
    apkg_files = [file for file in os.listdir(cwd) if file.endswith(".apkg")]
    for deck_file in apkg_files:
        import_anki_deck(cwd + deck_file)
