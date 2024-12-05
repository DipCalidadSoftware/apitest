import requests

url = "https://www.metmuseum.org/met-publications/the-metropolitan-museum-journal-volume-2-1969?_rsc=1t83c"

payload = {}
headers = {
  'accept': '*/*',
  'accept-language': 'es,en-US;q=0.9,en;q=0.8',
  'cookie': 'visid_incap_1662004=ygdA42s8QUSUThuukmH0DcnMcGYAAAAAQUIPAAAAAABD8uHwjRxv6oz3qy536Vs4; _gcl_au=1.1.1377577537.1718669097; visid_incap_1661922=7IOtO7G3QwSkqH0ufeeviifPcGYAAAAAQUIPAAAAAABFzEC2k6+UXpzCGe/rLkX7; _tt_enable_cookie=1; _ttp=fe-j9aI6N352NJ9aI7O3zIxfI7t; __qca=P0-1749156259-1718669098069; QuantumMetricUserID=09aed76b23fc2ef1f02e842fec6f9390; visid_incap_1661977=km3gmIpnRk6CnL2lfalD4TrPcGYAAAAAQUIPAAAAAADdyeRnWLqLnZosUqthkvLR; NEXT_LOCALE=en; _hjSessionUser_3360071=eyJpZCI6ImUzMmJiOGJmLTZhZTEtNWViYS05ZGYzLTA3ZmQ2ZTFmZmM2MiIsImNyZWF0ZWQiOjE3MTg2NjkzMjMwMjksImV4aXN0aW5nIjpmYWxzZX0=; _gid=GA1.2.408562477.1719237978; incap_ses_1474_1661922=lso0NfJPz1jXrSxrQ7N0FGt9eWYAAAAA8URw65c7kEfd+04aRd987g==; incap_ses_789_1661922=YH0bUyccolnZytQjaRfzCmt9eWYAAAAACUdi7XE2uGZMShnYB9+Qlw==; incap_ses_298_1661922=WH+sSZKxOSYxmXwYg7UiBGx9eWYAAAAAk3VrVFyN4MPw33iPoiNOHQ==; incap_ses_1241_1661922=Y0PiDRJitAvmsH4PBOs4EWt9eWYAAAAAGU6Ylwu1SlneBWnQXYgVfQ==; incap_ses_1475_1661922=eldENk+J8j25QAkQwkB4FGt9eWYAAAAAf12os6Jka0nUVbpxtmWSiA==; incap_ses_1473_1661922=SWVYU14GyS23rsUOxyVxFGt9eWYAAAAAFJla6GhXAgFkqrzUI80Ufg==; incap_ses_1696_1661922=2QAbYDBuqBFucFtPFmeJF2t9eWYAAAAA0HakMJeUoqG5/Dy1g68GzA==; incap_ses_1312_1661922=Y5gzToTXHlVs3HVuISk1Emx9eWYAAAAAjcW48u65fnmq0TaqTkoU3w==; incap_ses_1478_1661922=UBHCAHxZqRmjIQECPumCFGt9eWYAAAAA0AJDYPpKGusN1G9wsNs+Hg==; _parsely_session={%22sid%22:4%2C%22surl%22:%22https://www.metmuseum.org/%22%2C%22sref%22:%22%22%2C%22sts%22:1719260449382%2C%22slts%22:1719237978619}; _parsely_visitor={%22id%22:%22pid=aa486165-0b24-4cc7-9810-f6d934ef84be%22%2C%22session_count%22:4%2C%22last_session_ts%22:1719260449382}; QuantumMetricSessionID=624b12b2fb375451609d91ab63b5367a; incap_ses_1240_1661922=kjU+GPOwA2hW/vpthV01ESPVeWYAAAAAGBdgqkGT9JNVpf3LIIwB9A==; incap_ses_1477_1661922=7m6fcQ/FQh6gNtNZv1t/FCPVeWYAAAAAKBUhtmHLJUKnWTtmhfmMmQ==; incap_ses_1298_1661922=6xnGdttQChZvIhNsNGwDEiPVeWYAAAAArWOr2k0MC4L6GZGlNo1QQA==; incap_ses_1354_1661922=M9U0bUm+P3XVfKp36F/KEiPVeWYAAAAABA5HG2W1Ya/noET9FY/Diw==; incap_ses_1695_1661922=2WUfUyMIjHgB9yCnntmFFyPVeWYAAAAAtfppPd0L+u5XecaCjtFTFA==; _ga=GA1.2.198173188.1718669098; incap_ses_784_1661922=NHaANawuOjEq21fw9lPhCiPVeWYAAAAA7Tyyq3q+8/BBu/qiG8Av6w==; incap_ses_1694_1661922=9X5SUQioEVUij6YGGUyCFyPVeWYAAAAAXc7ZLdoDfn3F1dBRI/piHw==; incap_ses_786_1661922=QXcnZi+tAiQDam477W7oCiTVeWYAAAAApM7jEc2eTlYcoBCjRCPIfw==; _gat_UA-72292701-1=1; _ga_Y0W8DGNBTB=GS1.1.1719260449.6.1.1719260723.0.0.0',
  'next-router-prefetch': '1',
  'next-router-state-tree': '%5B%22%22%2C%7B%22children%22%3A%5B%5B%22locale%22%2C%22en%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22(navigation)%22%2C%7B%22children%22%3A%5B%22search-results%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fsearch-results%3Fq%3D%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D',
  'next-url': '/en/search-results',
  'priority': 'u=1, i',
  'referer': 'https://www.metmuseum.org/search-results?searchFacet=Publications',
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
