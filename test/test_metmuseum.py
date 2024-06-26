import pytest
import requests

def test_get1():
    url = "https://www.metmuseum.org/api/site_search?searchFacet=Events&page=1"
    response = requests.get(url)
    assert response.status_code == 200


def test_get2():
    url = "https://www.metmuseum.org/api/site_search?searchFacet=Exhibitions&page=1"
    response = requests.get(url)
    assert response.status_code == 200

def test_get3():
    url = "https://www.metmuseum.org/api/site_search?searchFacet=Learn&page=1"
    response = requests.get(url)
    assert response.status_code==200