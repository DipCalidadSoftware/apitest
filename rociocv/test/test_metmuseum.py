import pytest

import requests

def test_load():
    url = "https://store.metmuseum.org/customer/section/load/?sections=directory-data&force_new_section_timestamp=false&_=1718837166261"
    response = requests.get(url)
    assert response.status_code == 200

def test_additem_store():
    url = "https://store.metmuseum.org/checkout/cart/add/uenc/aHR0cHM6Ly9zdG9yZS5tZXRtdXNldW0ub3JnL3Zhbi1nb2doLWlyaXNlcy1nbGFzcy12YXNlLTgwMDU2Njc4/product/191347/"
    response = requests.post(url)
    assert response.status_code == 200

def test_update_item():
    url = "https://store.metmuseum.org/checkout/sidebar/updateItemQty/?cartQtyUpdate=true"
    response = requests.post(url)
    assert response.status_code == 200

def test_delete_item():
    url = "https://store.metmuseum.org/checkout/sidebar/removeItem/"
    response = requests.post(url)
    assert response.status_code == 200
