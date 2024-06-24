import pytest
import requests

def test_get():
    url = "https://deploy.mopinion.com/config/e7ctu6gpktn1epj72y4ewdrnwdtnzqdejbp%22"
    response = requests.get(url)
    assert response.status_code == 200