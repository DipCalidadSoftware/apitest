import pytest
import requests


def test_search_articles():
    url = "https://www.metmuseum.org/api/site_search?=Text&searchFacet=Articles&page=1"
    response = requests.get(url)
    assert response.status_code == 200


def test_exhibitions_1999():
    url = "https://www.metmuseum.org/api/exhibitions/year/1999"
    response = requests.get(url)
    assert response.status_code == 200


def test_search_met_media():
    url = "https://www.metmuseum.org/api/site_search?searchFacet=MetMedia&page=1"
    response = requests.get(url)
    assert response.status_code == 200
