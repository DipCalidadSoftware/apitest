import requests

url = "https://www.metmuseum.org/es/about-the-met/collection-areas/the-american-wing"

payload = {}
headers = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'es-ES,es;q=0.9',
  'cache-control': 'max-age=0',
  'cookie': 'visid_incap_1661977=lU9BwdNWThycWP6I3AoDwkFUc2YAAAAAQUIPAAAAAAB5ZN4siSu/BVSYxKmf9Tdx; visid_incap_1661922=0p/7oGPQTwiUjRN0MHYgxkFUc2YAAAAAQUIPAAAAAABCLPSnu8FWI4SXPoIJDB4d; _gcl_au=1.1.114835655.1718834242; _fbp=fb.1.1718834242040.594453975842535756; _tt_enable_cookie=1; _ttp=7Gdf4spJTy8FXFIstYqmnZJQVu3; __qca=P0-1547810924-1718834242293; QuantumMetricUserID=0711770fb9e489eb90ab69deef0a6ca0; visid_incap_1662004=XNfBzGoHQm+XAReCY+I8ErpYc2YAAAAAQUIPAAAAAADokL9+Q5r9P/UzLkoQyOL+; _hjSessionUser_3360071=eyJpZCI6ImVhYmYzMTI4LWI1OGItNTA2ZS05MTBhLTVhZjk2NTMzZmIyOCIsImNyZWF0ZWQiOjE3MTg4MzUzODk4OTEsImV4aXN0aW5nIjpmYWxzZX0=; NEXT_LOCALE=es; _parsely_session={%22sid%22:2%2C%22surl%22:%22https://www.metmuseum.org/es%22%2C%22sref%22:%22%22%2C%22sts%22:1719195474328%2C%22slts%22:1718834242096}; _parsely_visitor={%22id%22:%22pid=57491b52-3a5f-4ade-a22d-df99b5bb39ae%22%2C%22session_count%22:2%2C%22last_session_ts%22:1719195474328}; _gid=GA1.2.143067609.1719195474; QuantumMetricSessionID=41cf41c5f6718957f825db88447d18e5; shell#lang=en; incap_ses_297_1661922=SZWIdoOfwl23+Il1BCgfBHLXeGYAAAAAyjsnbrgmP4fofJQ52TgvlA==; __RequestVerificationToken=nvRN2IoSgUISXmuMn4QoxsXbHWsgBWqqbn30ecnevMtNN2RjqlEJgjhjHQaDoG3KIypNg09Dz5p88jyEZM7HYHKSJO41; incap_ses_1479_1661922=zZB4DSbXQVUyCKSivHaGFKTXeGYAAAAAkwBa68UmkuHd95Mmpjaj7A==; incap_ses_1241_1661922=PjL1ZcmdqWXiVzsPBOs4EaTXeGYAAAAA8VHObBSAZOvM6v+fHtR56g==; website#lang=es; incap_ses_1452_1661922=oASERu0DUVrTj2BAYYomFFPYeGYAAAAAds7HW2kgOLrKo8WpgGtS5Q==; incap_ses_787_1661922=4gCWDP5Kw3OsUxrga/zrClPYeGYAAAAAqeRglJTLM6Zp9zkElznA/w==; incap_ses_1694_1661922=xUKBayyBX3coW/MFGUyCF1PYeGYAAAAA0wKdUrH4Zt/Pv9ExO4RCsA==; incap_ses_1474_1661922=GNuTWU314m46QthqQ7N0FFPYeGYAAAAA64B8Z7ZhaYCGycVpQSfxBQ==; incap_ses_1454_1661922=1iFhFB65mGrmA7uLXqUtFFTYeGYAAAAA/jv7aYGEoAO7I/daLNUFDw==; incap_ses_784_1661922=0DOjMz78JUv79Jrv9lPhClXYeGYAAAAAIexvPxHZ2xiNQMejsY6lsg==; incap_ses_1354_1661922=/6nsWvbLdw5OQux26F/KEljYeGYAAAAAeekiO2xbgzifaKuGEyECog==; incap_ses_1455_1661922=zc87WxjQJj+ECcot3TIxFGDYeGYAAAAA60KUiseS4HH0cp+5O4BnWw==; metNotificationBanner=visited; incap_ses_1254_1661922=kbDoKAidOW3VNnhtchpnEYvYeGYAAAAAFmZhP8Dy9QNOc7EnVXoDsQ==; incap_ses_1312_1661922=//IgOQAtlV4VaDJuISk1EozYeGYAAAAAPxr9WtYX0EPlMCdO1045cQ==; incap_ses_1697_1661922=04kvB1oZoigqslTzlPSMF4zYeGYAAAAAz/0+ew7YuR5KUMyT0Hl/Lg==; incap_ses_785_1661922=VN1APjSAZWPy733qcOHkCozYeGYAAAAA6AKtF2UKKGK6aL+l6LS+qg==; incap_ses_1693_1661922=hCnEIT6pZxQ/HP9hmr5+F4zYeGYAAAAAtudflSKvPKlQhVS/dAZ6hQ==; incap_ses_1240_1661922=o1lxL6jyp01Xl0xthV01EYzYeGYAAAAA/sKSfuHFif5u6VUtAw7oyA==; incap_ses_1695_1661922=6e/WZ4aQf1cIGGGmntmFF4zYeGYAAAAABE0p6x+PRkFDh/6dFIe3WQ==; incap_ses_1473_1661922=tU2sG+tWiU0wcOzFxCVxFIzYeGYAAAAA3jJVcxZqv8PgXqUVScNnyw==; _ga_Y0W8DGNBTB=GS1.1.1719195474.3.1.1719195791.0.0.0; _ga=GA1.2.803802806.1718834242; incap_ses_1298_1661922=P08lZZ1jX0/aVXVrNGwDEpDYeGYAAAAAC1Wf5vTRpKsUx1Ku5pBm4A==; incap_ses_786_1661922=JLwaEpYIuwfCvuk67W7oCpDYeGYAAAAAH9mMgqojG4CYY+nWQhSVHg==; incap_ses_1477_1661922=o7MBYSFedU3hIiBZv1t/FJDYeGYAAAAAcSLzVcMNTevOgM//YFStQA==; incap_ses_1242_1661922=hzcwYjySDlSoSAG0gng8EZDYeGYAAAAAxOIknn5Hmg/tu5cBdW7vTg==; incap_ses_78_1661922=ul+QZ08IwRRoXEwuqxwVAfXYeGYAAAAARzKDbhqpLDTgW29R99MRpw==; visid_incap_1661922=2O6CeHOMQimlwzQh/HvgDHpYc2YAAAAAQUIPAAAAAAAWP5xuhFy8BV4a1m8kJsOn; visid_incap_1662004=7yOdlxhIQimmos+q5jtBKC3OcGYAAAAAQUIPAAAAAAB/IdQIOPIb3AZKypFSrT0w',
  'priority': 'u=0, i',
  'referer': 'https://www.metmuseum.org/es/about-the-met/collection-areas',
  'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
