import pytest
import requests

def test_get():
    url="https://engage.metmuseum.org/admission/?promocode=52349"
    response = requests.get(url)
    assert response.status_code==200;
