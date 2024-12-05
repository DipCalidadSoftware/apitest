import requests

ENDPOINT = "https://images.metmuseum.org/CRDImages/ep/original/DT1567.jpg"

def test_can_all_endpoint():
    response = requests.get(ENDPOINT)
    print(response)
    assert response.status_code == 200