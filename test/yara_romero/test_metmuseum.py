import requests
import pytest


def test_get_1():
    url = "https://www.metmuseum.org/es/policies/visitor-guidelines?_rsc=1kxo2"
    response = requests.get(url)
    assert response.status_code == 200


def test_get_2():
    url ="https://www.metmuseum.org/es/art/collection/search?department=10&showOnly=highlights%7CwithImage&sortBy=Title&_rsc=1qglo"
    response = requests.get(url)
    assert response.status_code == 200


def test_get_3():
    url = "https://www.metmuseum.org/es/plan-your-visit/group-visits/college-and-university-groups"
    response = requests.get(url)
    assert response.status_code == 200