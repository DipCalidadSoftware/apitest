import requests
import config

ENDPOINT = "https://api.trello.com/1/cards/"+config.ID+"?key="+config.API_KEY+"&token="+config.TOKEN

def test_can_all_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200
    
    