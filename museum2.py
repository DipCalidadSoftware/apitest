import requests
import pytest
def test_get():
    #Muestra la lista de diferentes formas de pagos de membresias
    url="https://engage.metmuseum.org/members/membership/?promocode=52596"
    response = requests.get(url)
    assert response.status_code==200