import requests
import json

url = "https://www.metmuseum.org/api/global/newslettersignup"

payload = json.dumps({
  "emailAddress": "abcd|@prueba.com",
  "pageInfo": "web_footer",
  "currentPageId": None
})
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0',
  'Accept': '*/*',
  'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
  'Accept-Encoding': 'gzip, deflate, br, zstd',
  'Referer': 'https://www.metmuseum.org/art/collection/search/454611',
  'content-type': 'application/json',
  'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjI4OTE1NzkiLCJhcCI6IjYwMTMwODAyOCIsImlkIjoiMzA3YWUzNTQ0ZGYzYjhlNCIsInRyIjoiN2E1NDdiMjIyMGIzZmQ4OTE4OTA4ZWQ3YWU4NmJiODMiLCJ0aSI6MTcxOTI1OTA3MzkyMX19',
  'traceparent': '00-7a547b2220b3fd8918908ed7ae86bb83-307ae3544df3b8e4-01',
  'tracestate': '2891579@nr=0-1-2891579-601308028-307ae3544df3b8e4----1719259073921',
  'Origin': 'https://www.metmuseum.org',
  'Connection': 'keep-alive',
  'Cookie': 'visid_incap_1662004=h6cfbMFFRGKceFqwx9tjElXIcGYAAAAAQUIPAAAAAABICbXHZb8wJ7WVbODq89ag; NEXT_LOCALE=en; _gcl_au=1.1.1297058425.1718667404.831794995.1718837023.1718837067; _ga_Y0W8DGNBTB=GS1.1.1719257356.5.1.1719259055.0.0.0; _ga=GA1.2.1682610493.1718667404; _parsely_visitor={%22id%22:%22pid=890be81b-65f9-4068-8191-d90a733c97e3%22%2C%22session_count%22:4%2C%22last_session_ts%22:1719257358153}; _fbp=fb.1.1718667405664.957241070984496388; _tt_enable_cookie=1; _ttp=bjvEyTWQQVkeypTA-HVWNvRwXFr; __qca=P0-735015117-1718667405394; QuantumMetricUserID=d5c5d1a625aaf1a2b133ad1223ed26b8; visid_incap_1661922=VkuryD12SquphCqLjZ7PoJrIcGYAAAAAQUIPAAAAAAC/IEGIzImidSN5QFARGNB1; visid_incap_2349797=v5FynAC1Q8ykJemF18Iv7L1bc2YAAAAAQUIPAAAAAAAeQyFfGvnpILF1sJfXS/nk; _ga_L6ZCHWX6DZ=GS1.1.1718836160.1.1.1718837152.0.0.0; _ga_80QRY9FZ67=GS1.1.1718836160.1.1.1718837152.0.0.0; _ga_BB83TXR9NF=GS1.1.1718849658.2.0.1718849658.60.0.0; _uetvid=b69f4d002e8d11efb20d15123af8d232; _svsid=3ee9ff54b98f33bce00062fa2c8499c7; xdibx=N4Ig-mBGAeDGCuAnRIBcoAOGAuBnNAjAOwEAcpAzCUQAwBMFNANCBgG6wB22hLu-qYmUrV6jFu1xcegloiQAbNCAAW2bBlyoA9NoDuBgHQBbAKbZj8XKfjHDAe0QBzbSBYLFy7QH54FsLj2SLCmALzGAIYAlpyW1rYAZH7GYGYAJlG24eZxNnaOTkn-sBHGGNFOnKHY9hicEWwAtLjYEdhRsG4gCniEJORUxGI0AL4sEDAYiKZsaKBpEQCeAgDaQgOidKQAbAC6Y-BQ0DOm3AKgdDQALKQAnNtzILPoIJ2yIDJr.SJkdLdXV32fEeb2YHzQKyBIBQL1BLE-ULSILQYIRBzeoDh4NQkJGePGR1gUSRqBAAFYIkQrttbuRGhRIKQiI0rgs0o1IMQIhyiAAzK40bb8giQCi8xrrH7bJk0IggEZAA___; _ga_DWPJYPP88X=GS1.2.1718837171.1.0.1718837182.49.0.0; __zlcmid=1MLmo6luFYIf1xn; website#lang=es; shell#lang=en; __RequestVerificationToken=N1ZpJ_dhxeIbmQkx8I7yuGsNykzJw_4v9TzhsS-RULiRkhDNlRaMxfyA7mppxj6G4wJkcRyDHeVHqv2GgQFrD87zu-k1; incap_ses_1693_1661922=cMN6Ek8UBwKBk8timr5+FwrJeWYAAAAAl15/ZP2YoQnNdk3QEtPRlw==; incap_ses_1298_1661922=aMK2YyuUO3SUSwhsNGwDEgvJeWYAAAAAvi8sVjKE+3dYNI5i3R0h/Q==; incap_ses_1454_1661922=D3UYWM9N+0vMdmXUYKUtFCPPeWYAAAAA+uX3p5w2UTg/MGEk5FuwWw==; _gid=GA1.2.1678550650.1719257358; _parsely_session={%22sid%22:4%2C%22surl%22:%22https://www.metmuseum.org/es/events/find-events?_gl=1*ylkbtk*_gcl_au*MTI5NzA1ODQyNS4xNzE4NjY3NDA0LjgzMTc5NDk5NS4xNzE4ODM3MDIzLjE3MTg4MzcwNjc.*_ga*MTY4MjYxMDQ5My4xNzE4NjY3NDA0*_ga_Y0W8DGNBTB*MTcxODgzNjEyOC4zLjEuMTcxODgzNzE0My4wLjAuMA..%22%2C%22sref%22:%22%22%2C%22sts%22:1719257358153%2C%22slts%22:1718836129621}; incap_ses_1254_1661922=MIonG9JjfAiemSJuchpnEaTMeWYAAAAAN+Ol60o3ZLyqt3fl/dNT0Q==; QuantumMetricSessionID=85d71141a09d9807fe7fc206291eae8d; incap_ses_1475_1661922=BvC5JvQyV0vvUGAQwkB4FJbPeWYAAAAA2X1J+d6n9Nz4g89jj73A1A==; incap_ses_787_1661922=3UZyVlbArgHcGKTga/zrChjMeWYAAAAAf9DDm1dwpu+h2ch/LJD86g==; incap_ses_1239_1661922=BgsUB3wvZjEUusB0BNAxEZnMeWYAAAAA6M+/qWV5hSQVoLvfzFwC4w==; incap_ses_1473_1661922=6oaPIhx3XRr0NREPxyVxFLrMeWYAAAAA1+uDTTI8gD76S3RTX2R9yw==; incap_ses_784_1661922=0jc6BT3asSpqL07w9lPhCr7MeWYAAAAA1hmsFnii0NC2DWAbuXtlRA==; incap_ses_1452_1661922=RFQNcUp2Ciqhb7WKY4omFKfMeWYAAAAAyBW7iRAwWVHM1mO9393pkw==; visid_incap_1661977=4nuS6SefQjGKdoG2U2VviK7MeWYAAAAAQUIPAAAAAACWTuCiORPhRS0PPVuRHlvB; incap_ses_1733_1661977=QeJjCxpt8VRLV+PJYdoMGK7MeWYAAAAAh2z2ABwkIX7hGqx/NHAcNw==; incap_ses_1695_1661922=dcfzS8e5LVQCDhqnntmFF7jOeWYAAAAAES20zb2YG5Y3ludiDSMhRg==; incap_ses_1476_1661922=HSHrP9p4wh5hxIe3QM57FATNeWYAAAAAc6LnG5eM5kLzpvsAR0YenQ==; incap_ses_1694_1661922=f1EQCm8R8QyqQaAGGUyCFwDPeWYAAAAAA8mrruWVED6Ry2WlK6sq7w==; incap_ses_786_1661922=Upm4AUmDbhkho2k77W7oCgbPeWYAAAAAKUnxPlT2lqSAPJg5hMGe6g==; incap_ses_1453_1661922=b5HrUVlBjWqlTHov4hcqFLXOeWYAAAAAujnunLYAxHV47dzdLqp1Ow==; incap_ses_1474_1661922=pxTCDhDnAQrRrn5rQ7N0FALPeWYAAAAAYjU1PPb6oa/byaq61rEAEg==; ObjectPageSet=0.285096398221839; incap_ses_1477_1661922=mBATThrXtTH4h8xZv1t/FCLPeWYAAAAAp6IF1VWaBGoVsPmzaCKMNA==; incap_ses_1354_1661922=7sp2ZHqzaHF3DqR36F/KEiPPeWYAAAAArKoKoCESCMlE3mQ/edollg==; incap_ses_1478_1661922=LyqbVESHhXOBVIACPumCFJbPeWYAAAAAX97jmqokJEOREIcu3bGlAg==; incap_ses_1312_1661922=006kT15Tt1+1TLxuISk1EiTPeWYAAAAAHOMP9qAMtQ9dlxrD4MGadg==; incap_ses_1733_1662004=wNPbJ93YOBGjj+XJYdoMGCTPeWYAAAAA9fUvY3kT7e3eTF83uWitdA==; incap_ses_297_1661922=ml8IAMN4bHcrtRZ2BCgfBCTPeWYAAAAAKjE0RRnTHNjsMlcM7UxNHA==; _hjSessionUser_3360071=eyJpZCI6IjFlZWMyM2YxLTY5MDAtNTMzMS1iNmUwLWNkYjk0NmY3OWVmZiIsImNyZWF0ZWQiOjE3MTkyNTg5MjA0MjMsImV4aXN0aW5nIjpmYWxzZX0=; _hjSession_3360071=eyJpZCI6IjEwMmI3MjJhLTE5MzctNGE1Yi1hZjFiLTBlNWI5OTJmNWU2MSIsImMiOjE3MTkyNTg5MjA0MjQsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MX0=; _gat_UA-72292701-1=1',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'Priority': 'u=1',
  'TE': 'trailers'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
