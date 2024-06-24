import pytest
import requests

def test_get():
    url = "https://www.metmuseum.org/exhibitions/sleeping-beauties-reawakening-fashion?_rsc=1ame0"
    response = requests.get(url)
    assert response.status_code == 200