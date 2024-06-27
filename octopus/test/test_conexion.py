from decouple import config
import requests
id = config('ID')
key = config('KEY')
url = config('URL')
token = config('TOKEN')

ENDPOINT = f"{url}/1/cards/{id}?key={key}&token={token}"

def test_can_all_endpoint():
    response = requests.get(ENDPOINT)
    print('asdsad')
    assert response.status_code == 200
    
def test_can_all_endpoint2():
    response = requests.get(ENDPOINT)
    print('asdsad')
    assert response.status_code == 200