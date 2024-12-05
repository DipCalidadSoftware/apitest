import requests
import pytest
def test_get():
    #Muestra proximas exhibiciones que habran
    url="https://www.metmuseum.org/es/exhibitions/upcoming"
    response = requests.get(url)
    assert response.status_code==200