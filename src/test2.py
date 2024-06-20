import requests

url = "https://www.metmuseum.org/art/collection/search?q=null&_rsc=1ddho"

payload = "x«VÊU²2Ô375635453´420³0ÓQJU²²ÐQª(V²24¨\u0005\u0000¯\b"
headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9,es;q=0.8',
  'content-type': 'text/plain',
  'origin': 'https://www.metmuseum.org',
  'priority': 'u=1, i',
  'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'cross-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
  'Cookie': 'visid_incap_1661922=+VS2F71ZRsinEQEBuyac45bPcGYAAAAAQUIPAAAAAABG8WN4ZcNv3H01rox60Axr; NEXT_LOCALE=en'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
