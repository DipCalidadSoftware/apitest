import requests

url = "https://www.metmuseum.org/art/collection/search?q=Wheat+Field+with+Cypresses&_rsc=1x9n3"

payload = {}
headers = {
  'accept': '*/*',
  'accept-language': 'es-ES,es;q=0.9',
  'cookie': 'NEXT_LOCALE=es; visid_incap_1661977=lU9BwdNWThycWP6I3AoDwkFUc2YAAAAAQUIPAAAAAAB5ZN4siSu/BVSYxKmf9Tdx; incap_ses_1614_1661977=5JDvTjw+mXrrLPXYhxRmFkFUc2YAAAAAMSv9lbgIEhneraZDQEAy0Q==; visid_incap_1661922=0p/7oGPQTwiUjRN0MHYgxkFUc2YAAAAAQUIPAAAAAABCLPSnu8FWI4SXPoIJDB4d; incap_ses_1693_1661922=mH85KIr9hW3IhK1dmr5+F0FUc2YAAAAAy3EGc5E9bfImQsaNiWp7lg==; _gcl_au=1.1.114835655.1718834242; _ga=GA1.2.803802806.1718834242; _gid=GA1.2.607595341.1718834242; _gat_UA-72292701-1=1; _fbp=fb.1.1718834242040.594453975842535756; _parsely_session={%22sid%22:1%2C%22surl%22:%22https://www.metmuseum.org/es/search-results?searchFacet=Art&q=Wheat+Field+with+Cypresses+%22%2C%22sref%22:%22%22%2C%22sts%22:1718834242096%2C%22slts%22:0}; _parsely_visitor={%22id%22:%22pid=57491b52-3a5f-4ade-a22d-df99b5bb39ae%22%2C%22session_count%22:1%2C%22last_session_ts%22:1718834242096}; _tt_enable_cookie=1; _ttp=7Gdf4spJTy8FXFIstYqmnZJQVu3; __qca=P0-1547810924-1718834242293; QuantumMetricSessionID=8b768e4b44b75757ea04bfcdfcfc37ba; QuantumMetricUserID=0711770fb9e489eb90ab69deef0a6ca0; _ga_Y0W8DGNBTB=GS1.1.1718834241.1.1.1718834256.0.0.0; incap_ses_1352_1662004=kwGZMvUeuBg2Zafq6ETDEuVHc2YAAAAAEFWUQwIu8G+TzAR3t37K8g==; visid_incap_1662004=7yOdlxhIQimmos+q5jtBKC3OcGYAAAAAQUIPAAAAAAB/IdQIOPIb3AZKypFSrT0w',
  'next-router-prefetch': '1',
  'next-router-state-tree': '%5B%22%22%2C%7B%22children%22%3A%5B%5B%22locale%22%2C%22es%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22(navigation)%22%2C%7B%22children%22%3A%5B%22search-results%22%2C%7B%22children%22%3A%5B%22__PAGE__%3F%7B%5C%22searchFacet%5C%22%3A%5C%22Art%5C%22%2C%5C%22q%5C%22%3A%5C%22Wheat%20Field%20with%20Cypresses%20%5C%22%7D%22%2C%7B%7D%2C%22%2Fes%2Fsearch-results%3FsearchFacet%3DArt%26q%3DWheat%2BField%2Bwith%2BCypresses%2B%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D',
  'next-url': '/es/search-results',
  'priority': 'u=1, i',
  'referer': 'https://www.metmuseum.org/es/search-results?searchFacet=Art&q=Wheat+Field+with+Cypresses+',
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