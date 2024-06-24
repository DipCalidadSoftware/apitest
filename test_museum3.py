import pytest
import requests

def test_post():
    url = "https://rl.quantummetric.com/metmuseum/hash-check"
    response = requests.get(url)
    assert response.status_code == 300