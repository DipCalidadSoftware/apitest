import requests
from assertpy.assertpy import assert_that, soft_assertions
from config import BASE_URI
import json



def test_login():
    url = f'{BASE_URI}/wp-json/api/v1/token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = "username=auto&password=apitest01."
    response = requests.post(url, headers=headers, data=payload)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    response_json = response.json()
    return f"{response_json.get('token_type')} {response_json.get('jwt_token')}"