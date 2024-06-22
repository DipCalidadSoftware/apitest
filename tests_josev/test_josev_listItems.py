import requests


def test_get_listItems():
    """This test request the GET method to retrieve a list of items in pagination one"""
    url = "https://www.metmuseum.org/api/site_search?q=picture&searchFacet=Primer&page=1"
    response = requests.get(url)
    assert response.status_code == 200

