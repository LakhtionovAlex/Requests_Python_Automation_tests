import os

import pytest
from dotenv import load_dotenv
from api.client import Client

load_dotenv()

LOGIN_STORE = os.getenv("LOGIN_STORE")
PASSWORD_STORE = os.getenv("PASSWORD_STORE")
URL_LOGIN = os.getenv("URL_LOGIN")


@pytest.fixture(scope="session")
def store_access_token():
    url = URL_LOGIN
    payload = {
        "login": LOGIN_STORE,
        "password": PASSWORD_STORE
    }
    response = Client.post(url, json=payload).json()
    yield response['access_token']
