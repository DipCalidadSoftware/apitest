import requests
import pytest
def test_get():
    #Muestra la coleccion de las obras de arte
    url="https://www.metmuseum.org/es/about-the-met/collection-areas"
    response = requests.get(url)
    assert response.status_code==200