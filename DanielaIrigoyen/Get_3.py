import requests

url = "https://googleads.g.doubleclick.net/pagead/viewthroughconversion/721115369/?random=1719261292290&cv=11&fst=1719261292290&bg=ffffff&guid=ON&async=1&gtm=45be46j0v889703438za200zb831496524&gcd=13l3l3l3l1&dma=0&tag_exp=0&u_w=1440&u_h=900&url=https%3A%2F%2Fengage.metmuseum.org%2Fevents%2Fpublic-guided-tours%2Fcollection-tours%2F%3F_gl%3D1*1jhrwln*_gcl_au*MTAzNTQ2ODEwOC4xNzE5MjU0MjM3LjIzOTI5ODgwMi4xNzE5MjYwMzk2LjE3MTkyNjA4NjU.*_ga*NjA2OTY0NDk3LjE3MTkyNTQyNDA.*_ga_Y0W8DGNBTB*MTcxOTI2MDM1Mi4yLjEuMTcxOTI2MTI4Ni4wLjAuMA..&ref=https%3A%2F%2Fwww.metmuseum.org%2F&hn=www.googleadservices.com&frm=0&tiba=Collection%20Tours%20%7C%20The%20Metropolitan%20Museum%20of%20Art&npa=0&pscdl=label_only_1&auid=1035468108.1719254237&uaa=x86&uab=64&uafvl=Not%252FA)Brand%3B8.0.0.0%7CChromium%3B126.0.6478.62%7CGoogle%2520Chrome%3B126.0.6478.62&uamb=0&uam=&uap=macOS&uapv=10.15.7&uaw=0&fledge=1&data=event%3Dgtag.config&rfmt=3&fmt=4"

payload = {}
headers = {
  'accept': '*/*',
  'accept-language': 'es-419,es;q=0.9',
  'cookie': 'ar_debug=1; receive-cookie-deprecation=1; IDE=AHWqTUlvxj6-KQFy44sTLdJ8GinlpQwj7swQmq8WqRLJ0_UZ61tw_Ci8c3hnHsLkKX4',
  'referer': 'https://engage.metmuseum.org/',
  'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-cookie-deprecation': 'label_only_1',
  'sec-fetch-dest': 'script',
  'sec-fetch-mode': 'no-cors',
  'sec-fetch-site': 'cross-site',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
  'x-client-data': 'CIi2yQEIo7bJAQipncoBCMmFywEIkqHLAQid/swBCIagzQEY9MnNAQ=='
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
