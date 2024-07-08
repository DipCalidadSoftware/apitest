import requests

url = "https://www.metmuseum.org/api/site_search?searchFacet=Exhibitions&q=radic&page=1"

payload={}
headers = {
  'accept': '*/*',
  'accept-language': 'es-419,es;q=0.9,en;q=0.8',
  'baggage': 'sentry-environment=vercel-production,sentry-release=f2ba8b33ec4f83862b997e64a4e4b16f10077ab7,sentry-public_key=fc26ffe1f7754e9aaa45cbb8fb82b860,sentry-trace_id=45cb89e3205b48b9957ea640de53ccb3',
  'cookie': 'visid_incap_1662004=2dNPyzm1QVqMwx/QGGffdtPJcGYAAAAAQUIPAAAAAAC2O2tOZqFzE2QE5vyfkIbo; incap_ses_1274_1662004=5e+LEWXVeD/oo79OVyiuEdTJcGYAAAAAoVkYfcEYsWvuVSzpigDPKQ==; _gcl_au=1.1.1421306911.1718668640; _parsely_session={%22sid%22:1%2C%22surl%22:%22https://www.metmuseum.org/es%22%2C%22sref%22:%22%22%2C%22sts%22:1718668640564%2C%22slts%22:0}; _parsely_visitor={%22id%22:%22pid=7ce6923d-412f-4362-b932-911e0c78e312%22%2C%22session_count%22:1%2C%22last_session_ts%22:1718668640564}; _fbp=fb.1.1718668640600.933420846902228706; _gid=GA1.2.1951679424.1718668641; _tt_enable_cookie=1; _ttp=GE4ANinF1Tb5TJ5WwvRkFA5jmvH; __qca=P0-884161558-1718668640918; QuantumMetricSessionID=41bc5b3d659fb7dc52eca73179a42929; QuantumMetricUserID=e77f1e0e5d7a8573c7cb14921d39ae9b; shell#lang=en; __RequestVerificationToken=VsfJu7oKxrl3ThkxuBahsb7rW39FZw3LPvN2_ishtjhDgy6le3ATBjsd5tW1OFGcPhLrC0YqtLzSBkQjbinsiHdiH5k1; visid_incap_1661922=l29jSIqXSDSWvu0yLe4UgWTNcGYAAAAAQUIPAAAAAACJBfP+8GutGtr9at/DtvED; incap_ses_298_1661922=365cXcUVIlQ/kajKgLUiBGTNcGYAAAAA63CG0CPTr4JECAEXZew1Vg==; incap_ses_1694_1661922=Nw+6LvnGVn5k8Uv/GEyCF2XNcGYAAAAAxHlQESgEQtj403uRwbpr1Q==; incap_ses_1474_1661922=jzIJc7luv0J6UCxlQ7N0FGXNcGYAAAAAHQWBpC8bP5UFfE9v6oaTOQ==; incap_ses_1698_1661922=C2k5KQE7Mn1TC0aSE4KQF2bNcGYAAAAAVEDZTmsIsumopjZEcYuraw==; incap_ses_1472_1661922=rbilXmoUl0yOSRocRphtFGXNcGYAAAAAGUyYEG1p5dcN5daqi5MY5w==; incap_ses_1696_1661922=7cyLDOdupwGrIx1JFmeJF2XNcGYAAAAANH/ixnh7KZEXx8/GlEM9gA==; incap_ses_1476_1661922=RkC+FdnuEHgfUxSwQM57FJPNcGYAAAAAme1oqhBvGEZ0UWnVJPDwaQ==; incap_ses_788_1661922=tKjDTuD1fGM/vGmB6onvCpPNcGYAAAAAktJCxuXZNpw8z/ZKtMwYEQ==; incap_ses_1475_1661922=MI+vMdChTyneZ6QJwkB4FJPNcGYAAAAADMHkBH/gnfKN+AZlQK1FIw==; incap_ses_787_1661922=ZkKUH8rfmX0qekrba/zrCpTNcGYAAAAAYVgKxUfTBYYnLyCwIOvdcA==; incap_ses_297_1661922=qIA5BHE9lE+oogYmAigfBJTNcGYAAAAAgDENZAKWBI6E5K5r7Ni0ow==; incap_ses_1697_1661922=7KK7Ko8rYCqraZ/tlPSMF5TNcGYAAAAABAG5eDSjnijTVQVs0z9WZA==; incap_ses_1239_1661922=JUSyaAWsWlcHX5wkAtAxEZTNcGYAAAAAuZwuwhS2BTT5/QtDfoPH9w==; incap_ses_1471_1661922=uk45MD9pLU0D2nR3xwpqFN/NcGYAAAAAwKLWOgjr8GoYnZrj+bIdZQ==; incap_ses_785_1661922=kDG2GZMgSiBPi63lcOHkCt/NcGYAAAAA3CUgvHsyUhhGKCi1rVLP4w==; incap_ses_1254_1661922=dVJWb2Aijm3/+jIgcBpnEd/NcGYAAAAAI3QHrlmxwhPTXC4XJkxdUw==; website#lang=en; ethn=6/17/2024 8:03:34 PM; incap_ses_1452_1661922=u7GoIgR84XmH69M7YYomFNfOcGYAAAAAsvDdSgfmqECrhnUxhqLFVw==; incap_ses_1695_1661922=prjYXXmkF0974XqgntmFF9fOcGYAAAAAhIQD77uFDKJ7x7ZSlteG3Q==; incap_ses_784_1661922=m7OleuuSVUOX08vp9lPhCtfOcGYAAAAAGBn7Bo4dMeERkBa7feveag==; incap_ses_789_1661922=sqzPR/09VAAA6BPVZhfzCtjOcGYAAAAAz7eUUXOrEne6BQRgmLflRQ==; NEXT_LOCALE=es; _ga=GA1.2.358294795.1718668640; _gat_UA-72292701-1=1; _ga_Y0W8DGNBTB=GS1.1.1718668640.1.1.1718669181.0.0.0',
  'priority': 'u=1, i',
  'referer': 'https://www.metmuseum.org/es/search-results?searchFacet=Exhibitions&q=radica',
  'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'sentry-trace': '45cb89e3205b48b9957ea640de53ccb3-afd3b6224a3e2f8c',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
