import pytest
import requests

def test_get():
    url = "https://www.metmuseum.org/mothra/collectionlisting/search?showOnly=withImage&department=8%7C62&perPage=40&sortBy=Title&offset=0%22"
    response = requests.get(url)
    assert response.status_code == 200