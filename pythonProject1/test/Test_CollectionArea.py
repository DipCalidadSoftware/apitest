import pytest
import requests

def test2_get ():
    url = "https://www.metmuseum.org/es/about-the-met/collection-areas/the-american-wing"
    response = requests.get(url)
    assert response.status_code == 200