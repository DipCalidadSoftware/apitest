import requests

url = "https://www.metmuseum.org/api/site_search?&page=2"

payload = {}
headers = {
  'accept': '*/*',
  'accept-language': 'es-419,es;q=0.9',
  'baggage': 'sentry-environment=vercel-production,sentry-release=f2ba8b33ec4f83862b997e64a4e4b16f10077ab7,sentry-public_key=fc26ffe1f7754e9aaa45cbb8fb82b860,sentry-trace_id=2bdd7decff7544e28182ffe2623e17cf',
  'cookie': 'visid_incap_1662004=/f+VAVlqTnWLKGOy0AcqlhPIcGYAAAAAQUIPAAAAAADz0K1szFp6h0+kOR/x0jSS; incap_ses_545_1662004=6xsIF8vk8yA3NGcYtDqQBxPIcGYAAAAAuWlfdiaAWx2CQ/YTH1PtLg==; NEXT_LOCALE=es; _gcl_au=1.1.923939922.1718668613; _tt_enable_cookie=1; _ttp=GTo7gFVR7Pk7087dQ-uAfYukKm3; __qca=P0-952754689-1718668613177; QuantumMetricUserID=edc1cb844bf8b4c605374bd0351259d5; shell#lang=en; __RequestVerificationToken=3P4yxtlDsFh_XT01ywVd0A1f-Bpp3iC23Phf69PNH-MNRWbRkvwPKSJPoeXFwbJn5lqqXrUGChih8Pvu-5VAocnXjSI1; visid_incap_1661922=hzxgYuY/T++79mpozKEYlmzOcGYAAAAAQUIPAAAAAABeAyf4c/e5GlYIvPt8h8gd; incap_ses_1694_1661922=NKejDqXbXgBD0Uz/GEyCF2zOcGYAAAAAKPwTxfr5sy5Oil10rJ3NPg==; _ga=GA1.2.1371690355.1718668613; visid_incap_1661977=H+EuIT20TAO87ZospnWSi3fOcGYAAAAAQUIPAAAAAADbybOWx8HQt0jVG5kppNKo; incap_ses_545_1661977=M7fHQYbQjwebWG0YtDqQB3fOcGYAAAAAKIhqxeOAMciO8ngDhs0oTA==; QuantumMetricSessionID=c7fe96f86b8a1b4e6d9758b1fdbc26e1; _parsely_session={%22sid%22:2%2C%22surl%22:%22https://www.metmuseum.org/es/search-results?q=sunflowers%22%2C%22sref%22:%22https://www.metmuseum.org/es%22%2C%22sts%22:1718829486728%2C%22slts%22:1718668613141}; _parsely_visitor={%22id%22:%22pid=16cff65a-3f1e-4eda-9067-960109883046%22%2C%22session_count%22:2%2C%22last_session_ts%22:1718829486728}; _ga_Y0W8DGNBTB=GS1.1.1718829629.2.0.1718829629.0.0.0; incap_ses_1312_1661922=Oo9ReG7ooRmWiIAhHyk1Ej1Cc2YAAAAAtX/nveJr3CvYytjb3Fbb2g==; incap_ses_1241_1661922=0akuKQgxpRpzcbjCAes4ET1Cc2YAAAAAXVlkUXHrePDLmy0oz89z1w==; incap_ses_8073_1661922=hNeJbAyEumGs/LmI0Q4JcD1Cc2YAAAAAqyt4qz/+Rgcd5LTdpRKAAQ==; incap_ses_1298_1661922=jb32HwOB+yE5Up8fMmwDEj5Cc2YAAAAALSYDWeg3rfaFNPjOY9DX7w==; incap_ses_545_1662004=ID06EGXKMwJ1ezcatDqQB5A+c2YAAAAA2BFiGL1/drr80zRMsCt94g==; visid_incap_1662004=M2opLTipR0KHFoTvKohXYh7OcGYAAAAAQUIPAAAAAAC+ShrzCsjRRySGgAgX28Ib',
  'priority': 'u=1, i',
  'referer': 'https://www.metmuseum.org/es/search-results?',
  'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'sentry-trace': '2bdd7decff7544e28182ffe2623e17cf-b6b774fd0d7cad01',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
