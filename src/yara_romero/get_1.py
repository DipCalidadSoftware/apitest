import requests

url = "https://www.metmuseum.org/es/policies/visitor-guidelines?_rsc=1kxo2"

payload = {}
headers = {
  'accept': '*/*',
  'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
  'next-router-state-tree': '%5B%22%22%2C%7B%22children%22%3A%5B%5B%22locale%22%2C%22es%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22(navigation)%22%2C%7B%22children%22%3A%5B%22policies%22%2C%7B%22children%22%3A%5B%5B%22slug%22%2C%22visitor-guidelines%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fes%2Fpolicies%2Fvisitor-guidelines%22%2C%22refresh%22%5D%7D%5D%7D%2Cnull%2C%22refetch%22%5D%7D%5D%7D%5D%7D%5D',
  'priority': 'u=1, i',
  'referer': 'https://www.metmuseum.org/es/plan-your-visit/met-cloisters',
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