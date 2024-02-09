import os

from api.client import Client


class ApiStore(Client):
    BASE_URL = os.getenv("BASE_URL")
    CLIENTS = os.getenv("CLIENTS")

    def get_all_clients_store(self, access_token):
        headers = {
            'Cookie': f'access_token={access_token}'
        }
        url = self.BASE_URL + self.CLIENTS
        return self.get(url, headers=headers)


api_store = ApiStore()
