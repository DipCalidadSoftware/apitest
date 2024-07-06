import pytest
from config import *

from src.wordpress_api.endpoint import Endpoint
from src.wordpress_api.api_request import WordpressRequest


@pytest.fixture
def get_token_login():
    url = f'{BASE_URI}{Endpoint.LOGIN.value}'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = f"username={USERNAME}&password={PASSWORD}."
    response = WordpressRequest.post(url,headers,payload)
    assert response.status_code == 200
    return response.json()
