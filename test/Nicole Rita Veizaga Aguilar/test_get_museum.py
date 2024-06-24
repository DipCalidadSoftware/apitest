import pytest
import requests

def test_get1():
    url= "https://www.metmuseum.org/api/site_search?q=ok&page=3"
    response=requests.get(url)
    assert response.status_code == 200

def test_get2():
    url= "https://www.metmuseum.org/api/site_search?q=ok&page=2"
    response=requests.get(url)
    assert response.status_code == 200

def test_get3():
    url= "https://metmuseum.zendesk.com/embeddable/config"
    response=requests.get(url)
    assert response.status_code == 200