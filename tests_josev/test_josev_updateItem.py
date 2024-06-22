import requests


def test_update_item():
    """This test request the POST method for updating article from cart - removed 1 article"""
    url = "https://store.metmuseum.org/checkout/sidebar/updateItemQty/?cartQtyUpdate=true"
    response = requests.post(url)
    assert response.status_code == 200
