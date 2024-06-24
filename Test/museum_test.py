import requests
import pytest
def test_get():
    #Nos muestra una lista de diferentes formas de pago de membresias
    url="https://engage.metmuseum.org/members/membership/?promocode=52596"
    response = requests.get(url)
    assert response.status_code==200