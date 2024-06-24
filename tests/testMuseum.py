import pytest
import requests

def test_get():
    url = "https://www.metmuseum.org/art/metpublications?_rsc=1pyte"
    response = requests.get(url)
    assert response.status_code == 200