import requests

url = "https://www.metmuseum.org/api/site_search?searchFacet=Events&page=1"

payload = {}
headers = {
  'accept': '*/*',
  'accept-language': 'en-BO,en;q=0.9,es-BO;q=0.8,es;q=0.7,en-GB;q=0.6,en-US;q=0.5',
  'baggage': 'sentry-environment=vercel-production,sentry-release=ae6dc81d6b4679ea0eb9c3699e5c1daa775ddfd8,sentry-public_key=fc26ffe1f7754e9aaa45cbb8fb82b860,sentry-trace_id=304610ba652d48669e6cda1ce1b18864',
  'cookie': 'visid_incap_1661922=SkqjYRIsSrylDLmvBL40jhC8emYAAAAAQUIPAAAAAADhvBpsdvNBjhwVUV/+2Q4u; _gcl_au=1.1.1557652916.1719319614; _gid=GA1.2.1223651870.1719319614; _fbp=fb.1.1719319617895.918941293649110251; _tt_enable_cookie=1; _ttp=sBtKOZJqeXocSYO-hESaf597JhB; __qca=P0-470444458-1719319615365; QuantumMetricUserID=5899fc15d06e05f6b9a7aaa5b4eec4a5; NEXT_LOCALE=en; visid_incap_2349797=0acXjxfmQpK4ghzkrIJ6hbvuemYAAAAAQUIPAAAAAAB/UhUHVwOL2ISqBokP82WQ; _ga_80QRY9FZ67=GS1.1.1719333089.1.0.1719333089.0.0.0; _ga_L6ZCHWX6DZ=GS1.1.1719333088.1.0.1719333090.0.0.0; incap_ses_1473_1661922=t7RETzChfBbP53sQxyVxFOwdfGYAAAAAUmJhEuU1DjV2wc5HNpUoUQ==; incap_ses_1312_1661922=o/YVWbw/DyZCdgFwISk1Eu0dfGYAAAAAyx57X4l0yJjQf+CPFwPuoQ==; _ga_Y0W8DGNBTB=GS1.1.1719410159.3.0.1719410159.0.0.0; incap_ses_788_1661922=J3Y4J7BBtkgp4dDP7InvCu0dfGYAAAAAwYohOoWszf0Y/+tXTxpn9g==; incap_ses_1698_1661922=XSavQb97MWFLViDiFYKQF+4dfGYAAAAALJqHQnP7tAnjSqHjHhIBfw==; incap_ses_1471_1661922=I9pNDyv77SwiVhPHyQpqFO4dfGYAAAAAlSpAI6WzXY1DfTdc0wAVxg==; _parsely_session={%22sid%22:4%2C%22surl%22:%22https://www.metmuseum.org/es/search-results?searchFacet=Videos%22%2C%22sref%22:%22%22%2C%22sts%22:1719410161775%2C%22slts%22:1719329598197}; _parsely_visitor={%22id%22:%22pid=7aae38bd-88e0-4f77-9003-7938514b6e77%22%2C%22session_count%22:4%2C%22last_session_ts%22:1719410161775}; _ga=GA1.2.1693983375.1719319614; _gat_UA-72292701-1=1; incap_ses_1240_1661922=u0sGdfkWm0YfoV9vhV01Ee8dfGYAAAAAeA6uveH4Xq/zGfipWHnYWA==; incap_ses_1477_1661922=WYMXKJsm2RRgtdKiwVt/FO8dfGYAAAAATGAAonOesdgdsdJncGi6wA==; QuantumMetricSessionID=e5e18f765da23e0458d24c26af44327e',
  'priority': 'u=1, i',
  'referer': 'https://www.metmuseum.org/es/search-results?searchFacet=Videos',
  'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'sentry-trace': '304610ba652d48669e6cda1ce1b18864-a5512d7bf37563f9',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
