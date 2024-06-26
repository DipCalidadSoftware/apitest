import requests

url = "https://www.metmuseum.org/api/site_search?q=the&searchFacet=Articles&page=1"

payload = {}
headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9,es;q=0.8',
  'baggage': 'sentry-environment=vercel-production,sentry-release=4585d0bae0d0d330d9632e07a8bda364a214f2c5,sentry-public_key=fc26ffe1f7754e9aaa45cbb8fb82b860,sentry-trace_id=0af165e86b4c4d179d3e02cac9451fce',
  'cookie': '_gcl_au=1.1.2033022923.1718822122; _gid=GA1.2.1037850266.1718822122; _parsely_session={%22sid%22:1%2C%22surl%22:%22https://www.metmuseum.org/%22%2C%22sref%22:%22%22%2C%22sts%22:1718822122381%2C%22slts%22:0}; _parsely_visitor={%22id%22:%22pid=7945c643-a495-4832-956d-4254e3bd34e0%22%2C%22session_count%22:1%2C%22last_session_ts%22:1718822122381}; _tt_enable_cookie=1; _ttp=3y9QOgdXcgw6X1OiRiZlR1kC4dC; _fbp=fb.1.1718822122898.448311044487312979; __qca=P0-1660362713-1718822122630; QuantumMetricSessionID=ac8426844bdefa83062cae733681752e; QuantumMetricUserID=fb64bbf959822cd92cf09d099f20b9e5; shell#lang=en; __RequestVerificationToken=LzmgysRi8OwzVT1Z1d2_t4AYNUSQb4Mxa-1yNRYko5S1kRFNMLssQS1H24rFRzMT9HVBEUB11TTwPTC53LQ5p9o2X301; visid_incap_1661922=hSfe4FTdRbyfg4rd6OdfcQElc2YAAAAAQUIPAAAAAAC55xFUY4TVPX9B4DNzjVXG; incap_ses_1474_1661922=nO5gZ6VS0Dy8VvFmQ7N0FAElc2YAAAAAx7Z+el0ec+bhP6784juG2g==; incap_ses_1298_1661922=bXxuXC1riijc/oMfMmwDEgIlc2YAAAAAt2c0ZPnvajRvpzXQ1jBLJw==; incap_ses_1697_1661922=VmJpRdtns2isBVPvlPSMFwUlc2YAAAAAmVtfUX5LMgUMJX5207cJ3g==; incap_ses_1693_1661922=xDiFdc/ByU2yu3hdmr5+Fx0lc2YAAAAAgAkvAk0T9KLcgZIlV3jlgw==; NEXT_LOCALE=es; _ga=GA1.2.1592596349.1718822122; _gat_UA-72292701-1=1; _ga_Y0W8DGNBTB=GS1.1.1718822122.1.1.1718822459.0.0.0; incap_ses_1478_1661922=2hDYdP4vvgLdCv/7PemCFDomc2YAAAAAC6QHQukH38BZUEqepy1P5g==; incap_ses_1479_1661922=mrxQDapgZD+Ep5eevHaGFDomc2YAAAAAdGzRNKnxDZLp8cMKL7V9WA==; incap_ses_297_1661922=ZmhYV5NcwBqzxmwnAigfBDomc2YAAAAACxwnlvZbb7CFaRp9tjshLQ==; incap_ses_1471_1661922=ATgkX4sUfjAcoy55xwpqFDsmc2YAAAAAOrA9iwtnfyCn23qjdUhJ8w==; incap_ses_1477_1661922=158XDZGYiEe0ShZVv1t/FDsmc2YAAAAAFYgC9daqVWwV+tFdz2UjKA==',
  'priority': 'u=1, i',
  'referer': 'https://www.metmuseum.org/es/search-results?q=the&searchFacet=Videos',
  'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'sentry-trace': '0af165e86b4c4d179d3e02cac9451fce-a39c83a1facd5e25',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
