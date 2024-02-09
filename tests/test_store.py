from api.store import api_store


def test_all_client_store_validate_response(store_access_token):
    response = api_store.get_all_clients_store(store_access_token)
    assert response.status_code == 200
