import requests

ENDPOINT = "https://collectionapi.metmuseum.org/public/collection/v1/search?q=sunflowers"

def test_can_all_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200