import requests

url = "https://www.metmuseum.org/mothra/collectionlisting/search?showOnly=withImage&department=8%7C62&perPage=40&sortBy=Title&offset=0%22"

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
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
  'Cookie': 'incap_ses_1242_1661922=btMVDR2BSRXGTge0gng8Ef7meGYAAAAAorT6W72CMhMwZp/i2BC3CA==; incap_ses_1473_1661922=eHdMdtY4vA05CfTFxCVxFLrneGYAAAAApoHm2GrzWZOca7Frq6YAaA==; visid_incap_1661922=enMa+VLLRae8Gz/TRaDjGv7meGYAAAAAQUIPAAAAAAClBrSACIjuG1UoP9RDF4qR; visid_incap_1662004=mnz+zDQRTVORY/9sZDfL6V3RcGYAAAAAQUIPAAAAAAApNZ0p2X9pR/ul0oObz8sa'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)