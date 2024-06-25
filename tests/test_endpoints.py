import json

import requests
import pytest

def test_get_1():
    url = "https://www.metmuseum.org/mothra/collectionlisting/search?q=Giovanni+di+Paolo+%28Giovanni+di+Paolo+di+Grazia%29&perPage=40&sortBy=DateDesc&offset=0&pageSize=0&showOnly=highlights"
    response = requests.get(url)
    assert response.status_code == 200

def test_get_2():
    url = "https://www.metmuseum.org/policies/privacy-policy?_rsc=vokxr"
    response = requests.get(url)
    assert response.status_code == 200

def test_post_1():
    url = "https://metmuseum.wd5.myworkdayjobs.com/wday/cxs/metmuseum/metmuseumcareers/jobs"

    payload = json.dumps({
        "appliedFacets": {
            "timeType": [
                "798df4ae1dba10c141e4aa3e1628006b"
            ]
        },
        "limit": 20,
        "offset": 0,
        "searchText": ""
    })
    headers = {
        'accept': 'application/json',
        'accept-language': 'en-US',
        'content-type': 'application/json',
        'cookie': 'wd-browser-id=39d9c86f-cfaa-432a-bde2-f116aa7d0cf9; CALYPSO_CSRF_TOKEN=3544c2a7-2d0a-4188-8c0b-e7dbfb732a29; PLAY_SESSION=512dccaafa749364fd2540ef5dc4c55360a4ae5e-metmuseum_pSessionId=drecvmb96l0lvsuhnbqbhejipi&instance=vps-prod-rl93cutg.prod-vps.pr503.cust.pdx.wd; wday_vps_cookie=552377354.53810.0000; __cf_bm=pgY9eH7onT4eSspqXddoeKE4BAur7N66hbPLMfS5jxY-1719344564-1.0.1.1-mxbAR0PaCSjjAPvseZagnkOVeBarDj75Y6ELWiirITCB1Dmlp5PahqxLL7Sg8Is_0tL6DlR.SiulBQiCoBj.Sg; __cflb=02DiuHJZe28xXz6hQKLeTYyWYf7NxYcM1NyretuyahP5v; _cfuvid=URpnaf0l8DIWbOX14wT9.s91MtYS6_gZx_NfhLvuW_Q-1719344564797-0.0.1.1-604800000; timezoneOffset=240; PLAY_SESSION=512dccaafa749364fd2540ef5dc4c55360a4ae5e-metmuseum_pSessionId=drecvmb96l0lvsuhnbqbhejipi&instance=vps-prod-rl93cutg.prod-vps.pr503.cust.pdx.wd; __cf_bm=QD5QvXcGDbsgxrBx050bNWPnBGksGRDzCArmWE91cfI-1719345743-1.0.1.1-jpu9hIznaqc5XL2h9Ah4IV1ijdf3pJbGkqtRfSx8GMtRpiSqKRWptLE1kyCJaLuka17sIilxoeIxBmFlJZKAiQ; _cfuvid=3NdNzPNQ4KZN0SpRctL34sHfL_4U6WHda1VpeZ2Hn1o-1719345743118-0.0.1.1-604800000; wday_vps_cookie=552377354.53810.0000',
        'origin': 'https://metmuseum.wd5.myworkdayjobs.com',
        'priority': 'u=1, i',
        'referer': 'https://metmuseum.wd5.myworkdayjobs.com/en-US/metmuseumcareers?timeType=798df4ae1dba10c141e4aa3e1628006b',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'x-calypso-csrf-token': '3544c2a7-2d0a-4188-8c0b-e7dbfb732a29'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response_data = response.json()

    assert response.status_code == 200
