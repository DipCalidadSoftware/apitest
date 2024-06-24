import pytest
import requests

def test_get():
    url = "https://player.vimeo.com/video/948738449/config/request?session=c5865d91ac4909f946ace1f6c763d22f3ffd579b1718668900&signature=85d049edfe65faabb57039c9b0392744&time=1718668900&expires=3600&referrer=https%3A%2F%2Fwww.metmuseum.org%2F"
    response = requests.get(url)
    assert response.status_code == 200