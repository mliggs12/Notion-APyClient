"""NotionAPI.py - Simple interface for personal testing.

API Reference: https://developers.notion.com/reference/intro
"""
from URL import URL
import os
import json
import requests


class NotionAPI:
    """Some text about the class."""
    def __init__(self):
        self.url = URL()
        self.headers = {'Authorization': 'Bearer ' + os.environ['NOTION_API_KEY'],
                        'Notion-Version': '2021-05-13'}

    def search(self):
        url = self.url.search

        return requests.request("POST", url, headers=self.headers)


if __name__ == "__main__":
    notion = NotionAPI()

    print(json.dumps(notion.search().json(), indent=4))
