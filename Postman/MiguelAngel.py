import requests

url = "https://www.metmuseum.org/es/art/collection/search?q=Miguel%20Angel"

payload = {}
headers = {
  'accept': '*/*',
  'accept-language': 'es-US,es;q=0.9,es-419;q=0.8,pt;q=0.7',
  'cookie': 'NEXT_LOCALE=es; _gcl_au=1.1.267895966.1718668123; visid_incap_1661922=r+eEcFE1QvSs3axqfD3SH2nLcGYAAAAAQUIPAAAAAAAgBDfERWGvTM3WoMipb1cL; QuantumMetricUserID=467e8b4792a79707cfc6c78e54b0ab53; _tt_enable_cookie=1; _ttp=sGtO3c82Jcq8xhHT8ULadUE9VLu; __qca=P0-1362978187-1718668125144; visid_incap_1661977=sFdrn+jtTiKb3OjeM3IffOTMcGYAAAAAQUIPAAAAAACQVgUPYJuHgVTEupYgpivZ; _gid=GA1.2.65721160.1718999267; _parsely_session={%22sid%22:3%2C%22surl%22:%22https://www.metmuseum.org/es%22%2C%22sref%22:%22https://metmuseum.github.io/%22%2C%22sts%22:1718999267522%2C%22slts%22:1718841308785}; _parsely_visitor={%22id%22:%22pid=c5a8cf8e-7ed2-444d-8e20-80c2a4d5cd92%22%2C%22session_count%22:3%2C%22last_session_ts%22:1718999267522}; QuantumMetricSessionID=4f19d4d87335cb3d46ad4ac365c88ec8; incap_ses_1452_1661922=2hCxRMc6XUOeleQ+YYomFAnZdWYAAAAA13FWPo32RzRMgf80UsxAOw==; _ga=GA1.2.711267614.1718668124; incap_ses_1616_1661977=X6/fKl3Y+W+GNEd2hy9tFmnedWYAAAAARMsW7fBjbNMf0mWcKHCCdA==; _gat_UA-72292701-1=1; _ga_Y0W8DGNBTB=GS1.1.1718999265.4.1.1719000863.0.0.0',
  'next-router-prefetch': '1',
  'next-router-state-tree': '%5B%22%22%2C%7B%22children%22%3A%5B%5B%22locale%22%2C%22es%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22(navigation)%22%2C%7B%22children%22%3A%5B%22search-results%22%2C%7B%22children%22%3A%5B%22__PAGE__%3F%7B%5C%22searchFacet%5C%22%3A%5C%22Art%5C%22%2C%5C%22q%5C%22%3A%5C%22mona%20lisa%5C%22%7D%22%2C%7B%7D%2C%22%2Fes%2Fsearch-results%3FsearchFacet%3DArt%26q%3Dmona%2Blisa%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D',
  'next-url': '/es/search-results',
  'priority': 'u=1, i',
  'referer': 'https://www.metmuseum.org/es/search-results?searchFacet=Art&q=Miguel+A',
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
