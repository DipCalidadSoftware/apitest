import requests

url = "https://ingest.quantummetric.com/horizon/metmuseum?T=B&u=https%3A%2F%2Fwww.metmuseum.org%2Fsearch-results%3FsearchFacet%3DArt%26q%3De&t=1718759841282&v=1718760296115&H=a03172667e19effd080dc589&s=3c356f9f316da61b36f7d15047f66c94&Q=2&S=8953&N=36&z=1"

payload = "x«V*P²2¬\u0005\u0000\bu\u0002\u0018"
headers = {
  'accept': '*/*',
  'accept-language': 'es-ES,es;q=0.9',
  'content-type': 'text/plain',
  'origin': 'https://www.metmuseum.org',
  'priority': 'u=1, i',
  'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'cross-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
