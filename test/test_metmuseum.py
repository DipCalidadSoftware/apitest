import pytest
import requests

def test_get1():
    url = "https://www.metmuseum.org/art/online-features/metcollects/man-ray-electricite"
    response = requests.get(url)
    assert response.status_code == 200


def test_get2():
    url = "https://www.metmuseum.org/articles/here-i-sette-my-thynge-to-sprynge"
    response = requests.get(url)
    assert response.status_code == 200

def test_get3():
    url = "https://www.metmuseum.org/met-publications/the-metropolitan-museum-journal-volume-19-20-1984-1985"
    response = requests.get(url)
    assert response.status_code == 200