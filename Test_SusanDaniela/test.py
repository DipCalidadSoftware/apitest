import pytest
import requests

def test_1():
    url = "https://www.metmuseum.org/sculptured/api/Events/Search?tab=Events&categories=Accessibility"
    response = requests.get(url)
    assert response.status_code == 200

def test_2():
    url = "https://engage.metmuseum.org/account/login/?returnUrl=/members/add-members/"
    response = requests.get(url)
    assert response.status_code == 200

def test_3():
    url = "https://www.metmuseum.org/dist/met.min.js?v=202406240300"
    response = requests.get(url)
    assert response.status_code == 200

