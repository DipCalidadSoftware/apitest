import requests


def test_post_item():
    """This test request the POST method for add article to bag"""
    url = ("https://store.metmuseum.org/checkout/cart/add/uenc/"
           "aHR0cHM6Ly9zdG9yZS5tZXRtdXNldW0ub3JnL3ZpbmNlbnQtcy1jb2xvcnMtd29yZHMtYW5kLXBpY3R1cmVz"
           "LWJ5LXZpbmNlbnQtdmFuLWdvZ2gtMTQwMTI5Njc~/product/11773/")
    response = requests.post(url)
    assert response.status_code == 200

