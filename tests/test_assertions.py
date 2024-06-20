import pytest
import requests
from config import BASE_URI


def unhandled_error():
    raise ValueError("Server error 500 status")



def test_get_assert():
    url = "https://www.metmuseum.org/art/collection/search?q=egipt&_rsc=ikp8v"
    response = requests.get(url)
    assert response.status_code == 200

def test_match():
    with pytest.raises(ValueError, match=r".* 500 .*"):
        unhandled_error()




def test_login_pytest():
    url = f'{BASE_URI}/wp-json/api/v1/token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = "username=auto&password=apitest01."
    response = requests.post(url, headers=headers, data=payload)
    response_data = response.json()
    assert response.status_code == 200
    assert response_data["token_type"] is not None
    assert response_data["jwt_token"] is not None

