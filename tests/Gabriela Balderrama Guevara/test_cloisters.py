import requests

def test_1():
    url = 'https://www.metmuseum.org/es/plan-your-visit/met-cloisters'
    response = requests.get(url)
    assert response.status_code ==200

def test_2():
    url = 'https://www.metmuseum.org/es/plan-your-visit'
    response = requests.get(url)
    assert response.status_code ==200

def test_3():
    url = 'https://engage.metmuseum.org/api/productioneventapi/events?productionSeasonIds=728093&performancestartdate=2024-07-01T04:00:00.000Z&performanceenddate=2024-09-01T04:00:00.000Z&mos=69'
    response = requests.get(url)
    assert response.status_code ==200