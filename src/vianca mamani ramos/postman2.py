import requests

url = "https://player.vimeo.com/video/948738449/config/request?session=c5865d91ac4909f946ace1f6c763d22f3ffd579b1718668900&signature=85d049edfe65faabb57039c9b0392744&time=1718668900&expires=3600&referrer=https%3A%2F%2Fwww.metmuseum.org%2F"

payload = {}
headers = {
  'Cookie': '__cf_bm=HHBf0j_fsyu9YqFWJWj_x93PwvEde545trRzIpdFgpQ-1719203896-1.0.1.1-3uqLTdRkoMa27YQgn1sK3XR2V4x4YJ4ILRj2a5nev_yG.qqRwczZ0y65KWwKlhitc.aaA167A1tfjxrFYKUuGw; _cfuvid=gOvlPQumb7WVLK8KNXn1pgElEi_40j2H8rBBdGLyvTI-1719203896837-0.0.1.1-604800000'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)