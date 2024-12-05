import requests

url = "https://cdn.quantummetric.com/qscripts/quantum-metmuseum.js"

payload = {}
headers = {
  'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
  'Referer': 'https://engage.metmuseum.org/',
  'sec-ch-ua-mobile': '?0',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
  'sec-ch-ua-platform': '"macOS"'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
