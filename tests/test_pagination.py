
import requests

def test_1():
    url = 'https://www.metmuseum.org/api/site_search?&page=2'
    response = requests.get(url)
    assert response.status_code == 200

def test_12():
    url = 'https://collectionapi.metmuseum.org/public/collection/v1/search?q=Medieval+Art'
    response = requests.get(url)
    assert response.status_code == 200


def test_2():
    url = 'https://engage.metmuseum.org/api/productioneventapi/events?productionSeasonIds=728092&performancestartdate=2024-06-19T21:07:24.321Z&performanceenddate=2024-08-01T21:07:24.321Z&mos=69'
    response = requests.get(url)
    assert response.status_code == 200