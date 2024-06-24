import pytest
import requests

def test_get():
    url="https://store.metmuseum.org/?utm_source=mainmuseum&utm_medium=metmuseum.org&utm_campaign=topnav-static"
    response = requests.get(url)
    assert response.status_code==200;
