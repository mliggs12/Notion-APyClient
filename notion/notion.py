"""Notion.py

Integration Name: Python-library
Environment variables:
Internal Integration Token: %NOTION_API_KEY%
Database ID: %NOTION_DB_ID%
"""
import os
import json
import requests
from requests import HTTPError

API_VERSION = 'v1'
BASE_URL = f'https://api.notion.com/{API_VERSION}/'
API_KEY = os.environ['NOTION_API_KEY']
DATABASE_ID = os.environ['NOTION_DB_ID']
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Notion-Version": "2021-05-13"}


def get_database(database_id):
    """Retrieves a `Database` obj. using the ID specified."""
    endpoint = BASE_URL + f'databases/{database_id}'
    r = requests.get(endpoint, headers=HEADERS)
    if r.status_code != 200:
        raise HTTPError(f"GET /databases/database_id/ {r.status_code}")

    return r.json()


if __name__ == "__main__":
    db = get_database(DATABASE_ID)
    print(json.dumps(db, indent=4))
