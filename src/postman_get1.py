import requests

url = "https://www.metmuseum.org/es/exhibitions"

payload = {}
headers = {
  'accept': '*/*',
  'accept-language': 'es-ES,es;q=0.9',
  'cache-control': 'no-cache',
  'cookie': 'NEXT_LOCALE=es; incap_ses_1696_1661922=hxe4W7etyDzcuV9PFmeJFzqBeWYAAAAAc6voGEAD43TUMJM99E06eQ==; incap_ses_784_1661922=hE+zcOyb2k1ON/jv9lPhCjqBeWYAAAAA1G5lxcP+iuEhFzAw2nIXdA==; incap_ses_1476_1661922=8UOoT3sk1FWPQTS3QM57FDqBeWYAAAAAfZUgjaHriUaMquslHAwZ/g==; incap_ses_1473_1661922=MrILDqpAKkoTTskOxyVxFDqBeWYAAAAAuPrhjghEhTlYabdiQ95kFw==; visid_incap_1661922=uxP+ONQgR9KEk+aOwa9zI5PCvWUAAAAAQkIPAAAAAAA147D6sJrE/ViZqci+TyRP; incap_ses_1453_1661922=lpLcHG46IWYLWz8v4hcqFDqBeWYAAAAAgPJZui0GXDWnCAqe/buTfQ==; incap_ses_787_1661922=a7XMekA51GUnNXjga/zrCvuYeWYAAAAAQ7soqfNPXazKHqQWmSgSpQ==',
  'next-router-prefetch': '1',
  'next-router-state-tree': '%5B%22%22%2C%7B%22children%22%3A%5B%5B%22locale%22%2C%22es%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22(navigation)%22%2C%7B%22children%22%3A%5B%22search-results%22%2C%7B%22children%22%3A%5B%22__PAGE__%3F%7B%5C%22searchFacet%5C%22%3A%5C%22Articles%5C%22%7D%22%2C%7B%7D%2C%22%2Fes%2Fsearch-results%3FsearchFacet%3DArticles%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D',
  'next-url': '/es/search-results',
  'pragma': 'no-cache',
  'priority': 'u=1, i',
  'referer': 'https://www.metmuseum.org/es/search-results?searchFacet=Exhibitions',
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
