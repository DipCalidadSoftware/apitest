import pytest
import requests

@pytest.mark.museo
def test_get():
    url = "https://www.metmuseum.org/art/collection/search?q=egipt&_rsc=ikp8v"
    response = requests.get(url)
    assert response.status_code == 200



def unhandled_error():
    raise ValueError("Server error 500 status")


def test_get_assert():
    url = "https://www.metmuseum.org/art/collection/search?q=egipt&_rsc=ikp8v"
    response = requests.get(url)
    assert response.status_code == 200

def test_match():
    ##TODO

    with pytest.raises(ValueError, match=r".* 500 .*"):
        unhandled_error()
