import pytest
import requests

from config import BASE_URI, USERNAME, PASSWORD


@pytest.fixture
def get_token_login():
    url = f'{BASE_URI}/wp-json/api/v1/token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = f"username={USERNAME}&password={PASSWORD}."
    response = requests.post(url, headers=headers, data=payload)
    assert response.status_code == 200
    return response.json()
    #return response_json.get('jwt_token', "NOT_FOUND")
