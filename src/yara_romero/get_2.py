import requests

url = "https://www.metmuseum.org/es/art/collection/search?department=10&showOnly=highlights%7CwithImage&sortBy=Title&_rsc=1qglo"

payload = {}
headers = {
  'accept': '*/*',
  'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
  'next-url': '/es/art/collection/search',
  'priority': 'u=1, i',
  'referer': 'https://www.metmuseum.org/es/art/collection/search?department=10&showOnly=highlights%7CwithImage',
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