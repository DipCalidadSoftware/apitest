import json
import requests


def test_login_authentication():
    url = "https://magento2-demo.magebit.com/rest/default/V1/integration/admin/token"
    headers = {'Content-Type': 'application/json'}
    payload = json.dumps({
        "username": "magebit",
        "password": "<Enter Password>"
    })
    response = requests.post(url, headers=headers, data=payload)
    response_data = response.json()
    assert response.status_code == 200
    assert response_data is not None
