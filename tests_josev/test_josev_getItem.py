import requests


def test_get_item():
    """This test request the GET method to retrieve item filtered"""
    url = ("https://api-cdn.yotpo.com/v3/storefront/store/UA2j691ALhaa1GiML20oGNunxsw7nTiICuIc49u4/product/11773/"
           "productFilters")
    response = requests.get(url)
    assert response.status_code == 200
