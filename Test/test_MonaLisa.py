import pytest
import requests

def test_get():
    url = "https://www.metmuseum.org/es/art/collection/search?q=mona%20lisa"
    response = requests.get(url)
    assert response.status_code == 200

