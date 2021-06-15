"""URL.py"""


class URL:
    """Handles all of the API endpoint URLs."""
    def __init__(self):
        pass

        self.base_url = 'https://api.notion.com/v1'

        # Databases
        retrieve_database = self.base_url + f'/databases/{"{database_id}"}'
        query_database = self.base_url + f'/databases/{"{database_id}"}/query'
        self.list_databases = self.base_url + '/databases'

        # Pages
        retrieve_page = self.base_url + f'/pages/{"{page_id}"}'
        create_page = self.base_url + '/pages'
        update_page_properties = self.base_url + f'/pages/{"{page_id}"}'

        # Blocks
        retrieve_block_children = self.base_url + f'/blocks/{"{block_id}"}/children'
        append_block_children = self.base_url + f'/blocks/{"{block_id}"}/children'

        # Users
        retrieve_user = self.base_url + f'/users/{"{user_id}"}'
        list_users = self.base_url + '/users'

        # Search
        self.search = self.base_url + '/search'
