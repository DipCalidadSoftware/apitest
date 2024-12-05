import pytest
import requests


def test_get_item():
    """This test request the GET method to retrieve item filtered"""
    url = ("https://api-cdn.yotpo.com/v3/storefront/store/UA2j691ALhaa1GiML20oGNunxsw7nTiICuIc49u4/product/11773/"
           "productFilters")
    response = requests.get(url)
    assert response.status_code == 200


def test_post_item():
    """This test request the POST method for add article to bag"""
    url = ("https://store.metmuseum.org/checkout/cart/add/uenc/"
           "aHR0cHM6Ly9zdG9yZS5tZXRtdXNldW0ub3JnL3ZpbmNlbnQtcy1jb2xvcnMtd29yZHMtYW5kLXBpY3R1cmVz"
           "LWJ5LXZpbmNlbnQtdmFuLWdvZ2gtMTQwMTI5Njc~/product/11773/")
    response = requests.post(url)
    assert response.status_code == 200


def test_update_item():
    """This test request the POST method for updating article from cart - removed 1 article"""
    url = "https://store.metmuseum.org/checkout/sidebar/updateItemQty/?cartQtyUpdate=true"
    response = requests.post(url)
    assert response.status_code == 200


def test_delete_item():
    """This test request the POST method for remove the bag items"""
    url = "https://store.metmuseum.org/checkout/sidebar/removeItem/"
    response = requests.post(url)
    assert response.status_code == 200


def test_get_listitems():
    """This test request the GET method to retrieve a list of items in pagination one"""
    url = "https://www.metmuseum.org/api/site_search?q=picture&searchFacet=Primer&page=1"
    response = requests.get(url)
    assert response.status_code == 200
