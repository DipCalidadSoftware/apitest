import pytest
import requests
pytest
def test_get():
    url = "https://www.metmuseum.org/es/art/collection/search?q=max%20liebermann"
    response = requests.get(url)
    assert response.status_code == 200