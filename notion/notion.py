"""Notion.py

    The `Notion` module is a thin wrapper to the endpoints of Notion API V1.

    Docs: https://developers.notion.com/docs

    Integration Name: Python-library
    Environment variables:
    Internal Integration Token: %NOTION_API_KEY%
    Database ID: %NOTION_DB_ID%
"""
import os
import logging
import json
import requests
from requests import HTTPError

BASE_URL = 'https://api.notion.com/v1'

INTEGRATION_TOKEN = os.environ['NOTION_API_KEY']
DATABASE_ID = os.environ['NOTION_DB_ID']    # my 'Desires' DB


class Notion:
    """Main interface for the module."""
    def __init__(self, integration_token, debug=False):
        """Instantiate a new :class:`Notion` interface with the required parameters
        for using the Notion API.

        :param integration_token: Internal Integration Token provided by Notion
        :param debug: logging; defaults to False
        """
        self.integration_token = integration_token
        self.headers = {"Authorization": f"Bearer {self.integration_token}",
                        "Notion-Version": "2021-05-13"}  # This will change
        self.DEBUG = debug

        if debug:
            logging.basicConfig(filename='./Logs/test.log',
                                filemode='w',
                                format='%(asctime)s - %(name)s - %(levelname)s:\n%(message)s',
                                level=logging.DEBUG)

    def execute(self, url=None, method="GET", headers=None, params=None):
        """Bootstraps and executes the `Request` for the `Notion` API methods.

        :param url: URL for the API endpoint sent by the API method
        :param method: HTTP method for the API method
        :param headers: Required HTTP Headers for Notion API authentication
        :param params: (optional) Dictionary to send in the body of the `Request`
        :return: `Response` object
        :rtype: dict
        """

        # Executes the request
        if method == "GET" or 'method' not in locals():
            r = requests.get(url, headers=self.headers, params=params)

        elif method == "POST":
            r = requests.post(url, headers=self.headers, json=params)

        else:
            return None

        # Log response content
        logging.debug(f"Response Content: {r.text}")

        if r.status_code != 200:
            raise HTTPError(f"{method} {url.split(BASE_URL)[1]} {r.status_code}")

        return r.json()

    # --------------
    # API Methods #
    # --------------

    def get_database(self, database_id):
        """Retrieves a `Database` obj. using the ID specified."""
        endpoint = BASE_URL + f'/databases/{database_id}/'

        return self.execute(endpoint)


if __name__ == "__main__":
    notion = Notion(INTEGRATION_TOKEN)
    db = notion.get_database(DATABASE_ID)
    print(json.dumps(db, indent=4))
