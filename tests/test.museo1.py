import pytest
import requests

def test_get():
    url = "https://www.metmuseum.org/api/site_search?searchFacet=Exhibitions&q=press&page=1"
    response = requests.get(url)
    assert response.status_code == 200
