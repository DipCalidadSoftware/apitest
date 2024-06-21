import requests

url = "https://www.metmuseum.org/es/art/collection/search?q=pablo%20picasso"

payload = {}
headers = {
  'accept': '*/*',
  'accept-language': 'es-ES,es;q=0.9',
  'cookie': 'NEXT_LOCALE=es; visid_incap_1661977=0Bb2gp7aRt+Q5PXqHmZNsDfDdWYAAAAAQUIPAAAAAADNO8WC388hLOM/sXtvyI7k; visid_incap_1661922=2T3ALH0GRoS+3LieY/44gTjDdWYAAAAAQUIPAAAAAAAYvGx2I5GGDhTGtZ2ydi9D; incap_ses_1312_1661922=2wlsKVmwLHOMlicjHyk1EjjDdWYAAAAAt6oE//XZdMM65VknrvnqKQ==; _gcl_au=1.1.1174271687.1718993729; _gid=GA1.2.219742832.1718993730; _tt_enable_cookie=1; _ttp=eYfwynWkYcw67S_rC_vyq5zqUun; __qca=P0-1190792298-1718993730025; QuantumMetricUserID=f0823aa9ec467452ff32bc691f24063f; incap_ses_297_1661922=LHhuEKOLJ2gPffNzBCgfBC3EdWYAAAAA8B0+73QWDeJAdpfix5ao1g==; incap_ses_1698_1661922=Pr0Me93jH1QoA/iVE4KQFy7EdWYAAAAAz/j7kQkbQ94JjC34wqvYng==; QuantumMetricSessionID=81ad43a6c759b5e22745e14db9a3830a; _parsely_session={%22sid%22:3%2C%22surl%22:%22https://www.metmuseum.org/es/search-results?q=gato%22%2C%22sref%22:%22https://www.metmuseum.org/es/art/collection%22%2C%22sts%22:1719002967764%2C%22slts%22:1718997757038}; _parsely_visitor={%22id%22:%22pid=25ac464a-5750-4de9-ba93-de103eed4908%22%2C%22session_count%22:3%2C%22last_session_ts%22:1719002967764}; incap_ses_788_1661922=+VhXNr/1C0n/GI+G6onvCk/tdWYAAAAAAl7a0Wj0yGRKNDKVVHJyUg==; incap_ses_1733_1661977=brWFBJZfaDYUT1/HYdoMGPrzdWYAAAAA8n5TtcWL3WJS+zjo2wDTrg==; incap_ses_1242_1661922=NJAAPL1+nWlyygZpgHg8EfvzdWYAAAAA9NP7jNUMTdi1iFDqZRqbww==; incap_ses_1697_1661922=ci3qXk4lXzbOv3vxlPSMF/rzdWYAAAAAnlXNP01Fo3JrwWgJqvR27A==; incap_ses_1241_1661922=g7X6Hqg5JT59dGzEAes4EfvzdWYAAAAAFx+l6phCZeZPktcGfEegug==; incap_ses_787_1661922=eahZJkIL1BKVQpnea/zrChP0dWYAAAAAFz8i/pSg3kP6BdQfYgOgrQ==; _gat_UA-72292701-1=1; _ga_Y0W8DGNBTB=GS1.1.1719002951.3.1.1719006414.0.0.0; _ga=GA1.2.756481389.1718993730',
  'next-router-prefetch': '1',
  'next-router-state-tree': '%5B%22%22%2C%7B%22children%22%3A%5B%5B%22locale%22%2C%22es%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22(navigation)%22%2C%7B%22children%22%3A%5B%22search-results%22%2C%7B%22children%22%3A%5B%22__PAGE__%3F%7B%5C%22searchFacet%5C%22%3A%5C%22Art%5C%22%2C%5C%22q%5C%22%3A%5C%22pablo%20picasso%5C%22%7D%22%2C%7B%7D%2C%22%2Fes%2Fsearch-results%3FsearchFacet%3DArt%26q%3Dpablo%2Bpicasso%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D',
  'next-url': '/es/search-results',
  'priority': 'u=1, i',
  'referer': 'https://www.metmuseum.org/es/search-results?searchFacet=Art&q=pablo+picasso',
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
