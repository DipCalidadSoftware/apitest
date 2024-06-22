import requests


def test_delete_item():
    """This test request the POST method for remove the bag items"""
    url = "https://store.metmuseum.org/checkout/sidebar/removeItem/"
    response = requests.post(url)
    assert response.status_code == 200
