import requests

#gets_the_privacy policies_of the met

url = "https://www.metmuseum.org/policies/privacy-policy?_rsc=vokxr"

payload = {}
headers = {
  'accept': '*/*',
  'accept-language': 'en,es;q=0.9,es-419;q=0.8',
  'cookie': 'visid_incap_1661922=pYGt4bMuQ2WLGlGWMm9+0HPJeWYAAAAAQUIPAAAAAADeNAFjmnbvrvWln6phAUhl; _gid=GA1.2.762659569.1719257477; _fbp=fb.1.1719257482350.113951836278216200; _tt_enable_cookie=1; _ttp=yZx18cthlqa68qkLVffB2rGEQKW; __qca=P0-2116220204-1719257479469; QuantumMetricUserID=7e52bc553515256201f878ad1cc0424d; visid_incap_1661977=mn9xkGibQCSNGvlHRcD54DDReWYAAAAAQUIPAAAAAAAvNuln8iz+8Pe86TR7suZt; visid_incap_1662004=sBwjYDLFR6an8RBoNn2QB3LReWYAAAAAQUIPAAAAAADUC4sumwDzT3s5kqmJ2Kwc; NEXT_LOCALE=en; _hjSessionUser_3360071=eyJpZCI6ImE0M2RmM2VmLTZjMmUtNWY2OC1iYTU3LWEyMjFmOTk2YTgyOCIsImNyZWF0ZWQiOjE3MTkyNTk1MTUzMTMsImV4aXN0aW5nIjp0cnVlfQ==; visid_incap_2349797=otK/278dQwOqmhai1KqKdbzweWYAAAAAQUIPAAAAAABdvXkQQfHtmuAQiEhtLhzD; _gcl_au=1.1.1860187831.1719257476.1249137014.1719288431.1719288430; _ga_L6ZCHWX6DZ=GS1.1.1719288430.2.1.1719288673.0.0.0; _ga_80QRY9FZ67=GS1.1.1719288430.2.1.1719288673.0.0.0; _ga_Y0W8DGNBTB=GS1.1.1719337161.6.0.1719337161.0.0.0; _ga=GA1.2.1063765128.1719257476; QuantumMetricSessionID=e6d7268e7502da80689b0dd319977543; _parsely_session={%22sid%22:6%2C%22surl%22:%22https://www.metmuseum.org/policies/terms-and-conditions%22%2C%22sref%22:%22https://engage.metmuseum.org/%22%2C%22sts%22:1719342864836%2C%22slts%22:1719337161001}; _parsely_visitor={%22id%22:%22pid=3b197922-8381-4785-a86c-824c4b94bef1%22%2C%22session_count%22:6%2C%22last_session_ts%22:1719342864836}; incap_ses_1343_1661922=ZB7lfzXJLHFPJFRsd0ujEgcme2YAAAAA5y+1F2/iU0vxkTMulAFLiw==; incap_ses_887_1661922=MOSgZKfEYirb2UtC5EFPDF8Ve2YAAAAAeAK75pLYFk7D796tc7V7yQ==; visid_incap_1661922=hLyuhFFWRuOOYr5wUtdaws7TeWYAAAAAQUIPAAAAAADAV73j97aSlql0r0Xs9TRm',
  'next-router-prefetch': '1',
  'next-router-state-tree': '%5B%22%22%2C%7B%22children%22%3A%5B%5B%22locale%22%2C%22en%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22(navigation)%22%2C%7B%22children%22%3A%5B%22policies%22%2C%7B%22children%22%3A%5B%5B%22slug%22%2C%22terms-and-conditions%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fpolicies%2Fterms-and-conditions%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D',
  'next-url': '/en/policies/terms-and-conditions',
  'priority': 'u=1, i',
  'referer': 'https://www.metmuseum.org/policies/terms-and-conditions',
  'rsc': '1',
  'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
