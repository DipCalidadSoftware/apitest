import requests

url = "https://deploy.mopinion.com/config/e7ctu6gpktn1epj72y4ewdrnwdtnzqdejbp%22"

payload = ""
headers = {
  'accept': '/',
  'accept-language': 'es-419,es;q=0.9',
  'origin': 'https://player.vimeo.com',
  'priority': 'u=1, i',
  'referer': 'https://player.vimeo.com/',
  'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'cross-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)