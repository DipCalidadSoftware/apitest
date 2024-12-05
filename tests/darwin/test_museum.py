import requests
import pytest

def test_endpoint1():
    url = "https://www.metmuseum.org/api/site_search?q=the&searchFacet=Articles&page=1"
    response = requests.get(url)
    assert (response.status_code == 200)
  

def test_endpoint2():
    url = "https://www.metmuseum.org/about-the-met/collection-areas"
    response = requests.get(url)
    assert (response.status_code == 200)


def test_endpoint3():
    url = "https://www.metmuseum.org/exhibitions"
    response = requests.get(url)
    assert (response.status_code == 200)
