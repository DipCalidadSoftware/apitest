import pytest
import requests

def test_get1():
    url = "https://www.metmuseum.org/es/exhibitions"
    response = requests.get(url)
    assert response.status_code == 200


def test_get2():
    url = "https://www.metmuseum.org/api/site_search?searchFacet=Primer&page=1"
    response = requests.get(url)
    assert response.status_code == 200

def test_get3():
    url = "https://www.metmuseum.org/es/exhibitions/sleeping-beauties-reawakening-fashion"
    response = requests.get(url)
    assert response.status_code == 200