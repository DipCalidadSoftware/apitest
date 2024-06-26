import requests
import pytest

def test_endpoint1():
    url = "https://www.metmuseum.org/met-publications/the-metropolitan-museum-journal-volume-2-1969?_rsc=1t83c"
    response = requests.get(url)
    assert (response.status_code == 200)
  

def test_endpoint2():
    url = "https://www.metmuseum.org/_vercel/speed-insights/vitals"
    response = requests.get(url)
    assert (response.status_code == 200)


def test_endpoint3():
    url = "https://www.metmuseum.org/exhibitions?_rsc=1t83c"
    response = requests.get(url)
    assert (response.status_code == 200)