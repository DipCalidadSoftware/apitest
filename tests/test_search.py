import requests

def test_12():
    url = 'https://collectionapi.metmuseum.org/public/collection/v1/search?q=Medieval+Art'
    response = requests.get(url)
    assert response.status_code == 200