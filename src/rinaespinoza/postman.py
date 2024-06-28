import requests

url = "https://www.metmuseum.org/art/collection/search?q=egipt&_rsc=ikp8v"

payload = {}
headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'cookie': 'NEXT_LOCALE=en; _gcl_au=1.1.1172134157.1718403443; _ga_Y0W8DGNBTB=GS1.1.1718403442.1.0.1718403442.0.0.0; _ga=GA1.2.1103666513.1718403443; _gid=GA1.2.192060730.1718403443; _gat_UA-72292701-1=1; _parsely_session={%22sid%22:1%2C%22surl%22:%22https://www.metmuseum.org/art/collection%22%2C%22sref%22:%22%22%2C%22sts%22:1718403442798%2C%22slts%22:0}; _parsely_visitor={%22id%22:%22pid=0dbccc79-6812-4411-9b7f-269bbabad671%22%2C%22session_count%22:1%2C%22last_session_ts%22:1718403442798}; _fbp=fb.1.1718403443130.1635181333093026; _tt_enable_cookie=1; _ttp=u-IfSJl2VvHGR3cPEcrYeJtwQYG; __qca=P0-2113638859-1718403443229; QuantumMetricSessionID=ae0deb9bacb4c351da8b5c4ae273ec87; QuantumMetricUserID=0beb9698ffd7248470603ba5ab4f6615',
  'next-router-state-tree': '%5B%22%22%2C%7B%22children%22%3A%5B%5B%22locale%22%2C%22en%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22(navigation)%22%2C%7B%22children%22%3A%5B%22art%22%2C%7B%22children%22%3A%5B%22collection%22%2C%7B%22children%22%3A%5B%22__PAGE__%22%2C%7B%7D%2C%22%2Fart%2Fcollection%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D',
  'next-url': '/en/art/collection',
  'priority': 'u=1, i',
  'referer': 'https://www.metmuseum.org/art/collection',
  'rsc': '1',
  'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
