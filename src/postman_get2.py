import requests

url = "https://www.metmuseum.org/api/site_search?searchFacet=Primer&page=1"

payload = {}
headers = {
  'accept': '*/*',
  'accept-language': 'es-ES,es;q=0.9',
  'baggage': 'sentry-environment=vercel-production,sentry-release=f0734f7c471e368fffd36bfdd8490a0ae7a7e22f,sentry-public_key=fc26ffe1f7754e9aaa45cbb8fb82b860,sentry-trace_id=bd2c8b525d2c44d2bcc9541fc6fc2a4f',
  'cache-control': 'no-cache',
  'cookie': 'NEXT_LOCALE=es; visid_incap_1661922=uxP+ONQgR9KEk+aOwa9zI5PCvWUAAAAAQkIPAAAAAAA147D6sJrE/ViZqci+TyRP',
  'pragma': 'no-cache',
  'priority': 'u=1, i',
  'referer': 'https://www.metmuseum.org/es/search-results?searchFacet=Exhibitions',
  'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'sentry-trace': 'bd2c8b525d2c44d2bcc9541fc6fc2a4f-b3a79f14e4136c80',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
