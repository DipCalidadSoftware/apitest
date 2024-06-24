import requests

url = "https://player.vimeo.com/video/948738449/config/request?session=c5865d91ac4909f946ace1f6c763d22f3ffd579b1718668900&signature=85d049edfe65faabb57039c9b0392744&time=1718668900&expires=3600&referrer=https%3A%2F%2Fwww.metmuseum.org%2F"

payload = ""
headers = {
  'accept': '/',
  'accept-language': 'es-419,es;q=0.9',
  'origin': 'https://player.vimeo.com',
  'priority': 'u=1, i',
  'referer': 'https://player.vimeo.com/',
  'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'cross-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
  'Cookie': '__cf_bm=PLeF5wCpT9t87exIRGNIqFEU5BQEGJf9fvXXRSTcPuc-1719199636-1.0.1.1-tycxgnBnWPNFNpRrCi9WRePoCcLTGl8ifQ33k1e8uBuQs0KmBl1Jfdswen791Ep1Xw.QoDgUcv1p8GTyHZIikg; _cfuvid=1MiTaTPpKz8HepMmlJwfzDs8diicy3rqP.fcyBBT.44-1719199636998-0.0.1.1-604800000'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)