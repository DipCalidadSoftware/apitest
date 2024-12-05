import requests

url = "https://metmuseum.zendesk.com/embeddable/config"

payload = ""
headers = {
  'accept': '*/*',
  'accept-language': 'es-419,es;q=0.9',
  'cookie': '_tt_enable_cookie=1; _ttp=x5j2oBJ2N-DXDWcgdY8seLnWOr5; __qca=P0-332106606-1718668347138; QuantumMetricUserID=0397f230a937a494ac86ed917d6a65df; visid_incap_1661922=RteU/lbhRJufZA73/pQJsHHNcGYAAAAAQUIPAAAAAACIk96twcKbZNAGHApk4oXi; visid_incap_2349797=yRUR78T/RfO1wPA2/9aFbHzNcGYAAAAAQUIPAAAAAAAQoqVycyTz/VHFW8zBjXwS; visid_incap_1661977=AAd1x6rbT8+bkQhbGRp3ZADTcGYAAAAAQUIPAAAAAAC07908RCHE9SmiLRUIj0kx; _hjSessionUser_3360071=eyJpZCI6IjAzNzIzNDA1LTdlZTktNWExNC04NGM3LWMyNThjMDBhMTE4ZiIsImNyZWF0ZWQiOjE3MTg2NzY4NzA2NTAsImV4aXN0aW5nIjp0cnVlfQ==; visid_incap_1662004=ZksueiMyR6Cp+6sj3FykgRjucGYAAAAAQUIPAAAAAABS+c8u74yI5zNQwy7y3ljH; NEXT_LOCALE=es; __zlcmid=1MKmnpIfcCxMyB7; oscw_close_policy=IYIwxkA_; oscw_close_policy_ext=B4TwXkA_; _uetvid=0ab511402d1911ef8d47dd547986e11b; xdibx=N4Ig-mBGAeDGCuAnRIBcoAOGAuBnNAjAOwEAcAbEaQAwCcBALKQwDQgYBusAdtmrW1z5UxMpRLVyAJloBmNp1w8-qASERIANmhAALbNgy5UAehMB3SwDoAtgFNsN-LjvwbVgPaIA5iZBtNLR0TAH54RzBcDyRYOwBeGwBDAEtuJxc3ADJwmzB7ABNktwSHdNd3L29siNhEmwwU72443Dd7RABaXGwAT007DskCAikGfxBNPEISCiIJaTkAXzYIGAxEOw40UHzEnuEAbVFZ-ZkAVgBdZfAoaE27XmFQKWomWnJtkC30EFhCNhURxm4mGpBIRCugk-f1Q1ABaAOkPU0LQcJAgKR-RRsPhqER1xhoBhBFxQLEcyoslIUikV0W11WcGSWNQIGocwYZwAZtSOrQGCMOgxaIl8h1SKQ7GK7BLZFyiFzIHMzkQOscQdQzrItSBFkA__; _ga_DWPJYPP88X=GS1.2.1718677104.1.1.1718678091.39.0.0; _ga_BB83TXR9NF=GS1.1.1718677104.1.1.1718678107.60.0.0; _gcl_au=1.1.447418293.1718668346.1873629533.1718678268.1718678268; _ga_80QRY9FZ67=GS1.1.1718678184.2.1.1718679032.0.0.0; _ga_L6ZCHWX6DZ=GS1.1.1718678184.2.1.1718679032.0.0.0; _gid=GA1.2.415604139.1718831795; _gat_UA-72292701-1=1; _parsely_session={%22sid%22:3%2C%22surl%22:%22https://www.metmuseum.org/es%22%2C%22sref%22:%22%22%2C%22sts%22:1718831794691%2C%22slts%22:1718674576742}; _parsely_visitor={%22id%22:%22pid=49dcb04a-7649-4a8c-b291-452c4d34b948%22%2C%22session_count%22:3%2C%22last_session_ts%22:1718831794691}; QuantumMetricSessionID=82a15938c0570f322ac2038d1bc3809c; incap_ses_1698_1661922=HJxCeRO19GVvVSqUE4KQF8NKc2YAAAAAnv8h/B1kjRs9VVTS4kQRXQ==; _ga_Y0W8DGNBTB=GS1.1.1718831794.4.1.1718831812.0.0.0; incap_ses_1312_1661922=QP9hZRjBI0lxVYchHyk1EsNKc2YAAAAAGZbXLdubitY7qrPHkfeO7w==; _ga=GA1.2.263485882.1718668346; incap_ses_1620_1661977=rFhBEUSJZA+JxDRhfWV7FsNKc2YAAAAAUcUqagV9HZtdRp91FvKKMQ==; __cfruid=81c9dcdf56617c6d595005bf54766b0cce2167c1-1718832823',
  'if-none-match': 'W/"t1ntts988m1iv7"',
  'next-router-prefetch': '1',
  'next-router-state-tree': '%5B%22%22%2C%7B%22children%22%3A%5B%5B%22locale%22%2C%22es%22%2C%22d%22%5D%2C%7B%22children%22%3A%5B%22(navigation)%22%2C%7B%22children%22%3A%5B%22search-results%22%2C%7B%22children%22%3A%5B%22__PAGE__%3F%7B%5C%22q%5C%22%3A%5C%22met%5C%22%7D%22%2C%7B%7D%2C%22%2Fes%2Fsearch-results%3Fq%3Dmet%22%2C%22refresh%22%5D%7D%5D%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D',
  'next-url': '/es/search-results',
  'priority': 'u=1, i',
  'referer': 'https://www.metmuseum.org/es/search-results?q=met',
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
