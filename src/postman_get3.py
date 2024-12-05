import requests

url = "https://www.metmuseum.org/es/exhibitions/sleeping-beauties-reawakening-fashion"

payload = {}
headers = {
  'accept': '*/*',
  'accept-language': 'es-ES,es;q=0.9',
  'cache-control': 'no-cache',
  'cookie': 'NEXT_LOCALE=es; visid_incap_1661922=uxP+ONQgR9KEk+aOwa9zI5PCvWUAAAAAQkIPAAAAAAA147D6sJrE/ViZqci+TyRP; incap_ses_1475_1661922=nroNcxOL2FN7K4kQwkB4FHf5eWYAAAAAVLwUmsLQu2KCFAppgnAPyg==; incap_ses_1474_1661922=vh8eCnPBZmTH3KVrQ7N0FHf5eWYAAAAAnTwOifhPPj+u8xUqGCOpFg==; incap_ses_1254_1661922=vNc/FIoLTwl8XlBuchpnEXf5eWYAAAAADQyG7sjAQzHuoQR9mc+2DA==; incap_ses_1470_1661922=TDYNHsjss1S5/fAgS31mFHj5eWYAAAAADbGto+WPkkVrQKQtnBrnZA==; incap_ses_1695_1661922=lqLtAFB3GFXb+ECnntmFF3j5eWYAAAAA2/i6MQGFriL6UAYLKoeLmw==',
  'next-router-prefetch': '1',
  'next-router-state-tree': '%5B%22%22%2C%7B%22children%22%3A%5B%5B%22locale%22%2C%22es%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22(navigation)%22%2C%7B%22children%22%3A%5B%22search-results%22%2C%7B%22children%22%3A%5B%22__PAGE__%3F%7B%5C%22searchFacet%5C%22%3A%5C%22Visit%5C%22%7D%22%2C%7B%7D%2C%22%2Fes%2Fsearch-results%3FsearchFacet%3DVisit%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D',
  'next-url': '/es/search-results',
  'pragma': 'no-cache',
  'priority': 'u=1, i',
  'referer': 'https://www.metmuseum.org/es/search-results?searchFacet=Visit',
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
