import pytest
import requests

def test_getrequest1():
    url = "https://www.metmuseum.org/es/art/collection"
    response = requests.get(url)
    assert response.status_code == 200

def test_getrequest2():
    url = "https://www.metmuseum.org/es/art/collection/search?showOnly=withImage&department=1"
    response = requests.get(url)
    assert response.status_code == 200

def test_getrequest3():
    url = "https://store.metmuseum.org/clothing-accessories/scarves-wraps"
    response = requests.get(url)
    assert response.status_code == 200