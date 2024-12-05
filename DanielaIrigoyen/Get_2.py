import requests

url = "https://beacon.sojern.com/pixel/p/203605?f_v=v6_js&p_v=2&pc=GTM-T558NJV&sha256_eml=&sha1_eml=&md5_eml=&ccid=&vid=tou&cid="

payload = {}
headers = {
  'accept': '*/*',
  'accept-language': 'es-419,es;q=0.9',
  'cookie': 'cid=60c829c4-b83d-de48-20e9-a0222b11c1d4#1719187200000; ttdid=1444a6c8-6b3c-4d42-aaaa-cd2374dd695e; adfid=5250520703756536096; gid=CAESEErbaUXohQvRHjdXB5kak0w; apnid=284379625456796421; dc-adv=%5B%7B%22dc%22%3A%22NYC%22%2C%22et%22%3A%22vpr%22%2C%22hb%22%3A%22TheMetMuseum%22%7D%2C%7B%22dc%22%3A%22NYC%22%2C%22et%22%3A%22vpr%22%2C%22hb%22%3A%22TheMetMuseum%22%7D%2C%7B%22dc%22%3A%22NYC%22%2C%22et%22%3A%22vpr%22%2C%22hb%22%3A%22TheMetMuseum%22%7D%2C%7B%22dc%22%3A%22NYC%22%2C%22dt%22%3A%226%2F25%2F2024+6%3A%22%2C%22et%22%3A%22vcart%22%2C%22hb%22%3A%22TheMetMuseum%22%2C%22nt%22%3A%223%22%7D%2C%7B%22dc%22%3A%22NYC%22%2C%22et%22%3A%22vpr%22%2C%22hb%22%3A%22TheMetMuseum%22%7D%2C%7B%22dc%22%3A%22NYC%22%2C%22dt%22%3A%226%2F25%2F2024+6%3A%22%2C%22et%22%3A%22vcart%22%2C%22hb%22%3A%22TheMetMuseum%22%2C%22nt%22%3A%226%22%7D%2C%7B%22dc%22%3A%22NYC%22%2C%22dt%22%3A%226%2F25%2F2024+6%3A%22%2C%22et%22%3A%22vcart%22%2C%22hb%22%3A%22TheMetMuseum%22%2C%22nt%22%3A%226%22%7D%2C%7B%22dc%22%3A%22NYC%22%2C%22dt%22%3A%226%2F25%2F2024+6%3A%22%2C%22et%22%3A%22vcart%22%2C%22hb%22%3A%22TheMetMuseum%22%2C%22nt%22%3A%223%22%7D%5D; cid=60c829c4-b83d-de48-20e9-a0222b11c1d4#1719187200000',
  'referer': 'https://engage.metmuseum.org/',
  'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'script',
  'sec-fetch-mode': 'no-cors',
  'sec-fetch-site': 'cross-site',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
