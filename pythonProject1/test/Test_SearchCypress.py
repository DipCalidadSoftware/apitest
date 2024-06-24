import pytest
import requests

def test_get():
    url = "https://www.metmuseum.org/art/collection/search?q=Wheat+Field+with+Cypresses&_rsc=1x9n3"
    response = requests.get(url)
    assert response.status_code == 200