import pytest
import requests


from config import BASE_URI, USERNAME, PASSWORD
from wordpress_api.api_request import WordpressRequest
from wordpress_api.endpoint import Endpoint


@pytest.fixture
def get_token_login():
    url = f'{BASE_URI}{Endpoint.LOGIN.value}'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = f"username={USERNAME}&password={PASSWORD}."
    #response = requests.post(url, headers=headers, data=payload)
    response = WordpressRequest.post(url,headers,payload)
    assert response.status_code == 200
    return response.json()
    #return response_json.get('jwt_token', "NOT_FOUND")
