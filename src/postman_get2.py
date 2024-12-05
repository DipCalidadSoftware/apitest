import requests
import pytest

    url = "https://www.metmuseum.org/articles/here-i-sette-my-thynge-to-sprynge"

    payload = {}
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'es-ES,es;q=0.9',
        'cache-control': 'max-age=0',
        'cookie': 'visid_incap_1662004=B1WQXhbYSnOGWQ1wY2L92IHIcGYAAAAAQUIPAAAAAABzmg5iLqrSdngHEzGPk0yn; _gcl_au=1.1.328188438.1718669161; _fbp=fb.1.1718669161318.305302614342807946; _tt_enable_cookie=1; _ttp=DVA5m6PRUXvksWu4cGgOPcgJeUN; QuantumMetricUserID=95ba51922512d18e856fea16f3f1672d; __qca=P0-964168054-1718669162172; visid_incap_1661922=3bnXQlrjTh6g+H5LWlBn93fPcGYAAAAAQUIPAAAAAABknJrconIgVTap8elKR7Gp; visid_incap_1661977=jd6oRm7pS+aS+ARwipkDgnnPcGYAAAAAQUIPAAAAAADbTw5MQiNbhbRqnG+HUjeh; _hjSessionUser_3360071=eyJpZCI6ImExMTBjNjU1LTA2NjEtNTE1OC05ZDE3LWFjYmZkYTIwM2Q1NiIsImNyZWF0ZWQiOjE3MTg2NjkyOTg2NjgsImV4aXN0aW5nIjp0cnVlfQ==; _gid=GA1.2.1657747670.1719179890; NEXT_LOCALE=en; _parsely_session={"sid":8,"surl":"https://www.metmuseum.org/met-publications/the-metropolitan-museum-journal-volume-19-20-1984-1985","sref":"","sts":1719252506128,"slts":1719210938916}; _parsely_visitor={"id":"pid=94ea3e04-510f-4881-bdce-a407f0576c2e","session_count":8,"last_session_ts":1719252506128}; shell#lang=en; ASP.NET_SessionId=nhsuijyc5nsmerlj0kmo04cg; incap_ses_1479_1661922=7vf9T8FLtkM5DzSjvHaGFBu2eWYAAAAAqzAcaJDrV5VqIMs1hfBOxQ==; incap_ses_1452_1661922=4mekBTY0OT+y3KOKY4omFBq2eWYAAAAAdzVgrcZTEnA1kLzGZ6xW9g==; __RequestVerificationToken=o4dypnDasJXJUIXEtUjfEZeeOU0ngJIasCiMzBme3Q0JZNjmmjlmdI1Wpj5GaoBUofIJN064fo5i7246m_r4WU8ujtw1; incap_ses_1474_1661922=gdBQVZFeMUaJuWVrQ7N0FBu2eWYAAAAAxX9On8bPOgrRYCk7NBg1mA==; incap_ses_1476_1661922=P8xgT3++snsFD223QM57FBu2eWYAAAAA4joE/WYZwXVoOShcOMbFUA==; incap_ses_298_1661922=PWEiDyTK2V2RALMYg7UiBFm5eWYAAAAAxIh+fpihmH8g4iM84PFp6Q==; incap_ses_784_1661922=jjRHLD84JG97gTfw9lPhClm5eWYAAAAAk/jRBhTr4l37rlpjaMH4Jw==; _gat_UA-72292701-1=1; _ga_Y0W8DGNBTB=GS1.1.1719252506.6.1.1719253868.0.0.0; _ga=GA1.1.845469470.1718669161; incap_ses_1298_1661922=QfgtYxTgy1AYAvxrNGwDEmy7eWYAAAAAVObfPJJqDxDdTsL5tsnQgA==; incap_ses_297_1661922=rT02DJuqPC3i6AV2BCgfBG27eWYAAAAAHXHfr9hC4FELL8WoXJP5Fw==; QuantumMetricSessionID=6583653f673f6bf425b42ba8363ada40',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    assert response.status_code == 200

