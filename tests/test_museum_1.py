import pytest
import requests

def test_get():
    url="https://www.metmuseum.org/en/met-publications/along-the-riverbank-chinese-paintings-from-the-c-c-wang-family-collection?_rsc=qbzl6"
    response = requests.get(url)
    assert response.status_code==200;
