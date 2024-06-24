import pytest
import requests

def test_get():
    url = "https://www.metmuseum.org/art/collection/search?q=q&_rsc=1ddho"
    response = requests.get(url)
    assert response.status_code == 200