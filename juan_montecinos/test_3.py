import requests

ENDPOINT = "https://collectionapi.metmuseum.org/public/collection/v1/objects?objectID=437133"

def test_can_all_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200