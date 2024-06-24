import requests

ENDPOINT = "https://api.trello.com/1/cards/66712276ba3e713a97a105fb?key=39ad1240991f892d98ca7a43e516aa5e&token=ATTA7e6858c9c83947b73587f5ad3cf9f175a13eb9f95b821a3f78af068c07a46d1bABDDB9FB"

def test_can_all_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200
    
    