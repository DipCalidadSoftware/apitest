import pytest
import requests


def test_get():
    url = "https://www.metmuseum.org/art/collection/search?q=egipt&_rsc=ikp8v"
    response = requests.get(url)
    assert response.status_code == 200