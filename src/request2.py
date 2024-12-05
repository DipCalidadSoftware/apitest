import requests

url = "https://www.metmuseum.org/es/art/collection/search?showOnly=withImage&department=1"

payload = {}
headers = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'es-ES,es;q=0.9',
  'cache-control': 'max-age=0',
  'cookie': 'visid_incap_1662004=f19LzyYdRtS5CyqUs/dQsf7HcGYAAAAAQUIPAAAAAAAmtjTxk4z3aC6HUT+tYpOm; incap_ses_1616_1662004=TEXpSjD+tj5c2iZyhy9tFv7HcGYAAAAAYc/0/tEhRQHHZXuCVwZvXQ==; NEXT_LOCALE=es; _gcl_au=1.1.198007673.1718668089; _gid=GA1.2.944337709.1718668090; _tt_enable_cookie=1; _ttp=Dcep1BC4SVzuLQva9mwpxtJgj64; __qca=P0-538999123-1718668090034; _parsely_session={%22sid%22:1%2C%22surl%22:%22https://www.metmuseum.org/es%22%2C%22sref%22:%22%22%2C%22sts%22:1718668090895%2C%22slts%22:0}; _parsely_visitor={%22id%22:%22pid=9bfad46a-8848-4765-898d-d88db2f79b01%22%2C%22session_count%22:1%2C%22last_session_ts%22:1718668090895}; QuantumMetricSessionID=bf17ced484b33924484472556c60ff7a; QuantumMetricUserID=6d22dce3697c8137312a385f289edd03; aceSession=1vf69qTUtF3E5dTtrHZdrjFfLNHrgEXmhzmqL5SO+LosfwyuzHp5QNAFaOcWU55MKNkbuQ4QXWC1FKXI6IXxrLcFr9uhZnfFss7NJHxmxfsFRdGw793EmqhAAP4dfMdI/9Av4r2jFPX/sl0HHMWaF92K4OwnNDCMKZsoku/sVW6wkKve/04SFWaAE5N3raF4; nlbi_2349797=FO5CL27OBCeik0SnzMiLaQAAAABTIm//RYAtiKkluJ51JiSf; visid_incap_2349797=LhixJzVxTuetMBBVHie8mPbMcGYAAAAAQUIPAAAAAAB5xZezacLJ5qmPuMLJ6wqg; incap_ses_1616_2349797=fGQSWXMsc3B3TSxyhy9tFvfMcGYAAAAAMTLAsNNejnM6oN2IIC7lgA==; incap_ses_1254_1661922=uKmAQdcIdjoCQjIgcBpnEfjMcGYAAAAAuJ5Hb9LN8ZlOVau2+S146A==; visid_incap_1661922=NOyAPd2ySNm6X6k3uPhoLfjMcGYAAAAAQUIPAAAAAABcPUuwPLLBbicIYNrbG9Du; incap_ses_788_1661922=uWipDXIp4QlhAGmB6onvCvjMcGYAAAAAm3KlrDJwGewg0irt3t6ogA==; nlbi_2349797_2147483392=CvdcEouIxWlVgUeizMiLaQAAAACIqbBvZFvMZ8i71yaTvD6N; _ga_L6ZCHWX6DZ=GS1.1.1718668539.1.1.1718668554.0.0.0; _ga_80QRY9FZ67=GS1.1.1718668539.1.1.1718668554.0.0.0; _ga=GA1.2.1617797142.1718668090; shell#lang=en; incap_ses_1453_1661922=6ekFNBmTI2iffSng3xcqFDXPcGYAAAAA/vVGZ44rDppnbodniSDIhw==; incap_ses_298_1661922=8/gQVhZLUXvdD6rKgLUiBDXPcGYAAAAAE4j1/xJz/UiIEJUWhZQViQ==; incap_ses_1698_1661922=Bj2hTqni0Aibq0eSE4KQFzXPcGYAAAAAiAcR2OHLLV+kKN7U2Sz1/Q==; __RequestVerificationToken=HJp-goWa4m9CLNLrN64zzDdlTLXoHrCtfB-1fljyqxGnTTCsmQzFwaMn3ALqcCwBYsi5yIcYodWxTQo7BvPP87Zv3O81; incap_ses_1696_1661922=VlKRZE25Oj0i7R5JFmeJFzXPcGYAAAAAZ/hHFRK+WaUPZ1y6BmeQ6A==; incap_ses_1476_1661922=zRLzVY1Rozxp4xWwQM57FDbPcGYAAAAAuiznli6pyroZ0j64n1WakQ==; _gat_UA-72292701-1=1; visid_incap_1661977=mpicQwhGSZuO0yVTFty/4l/PcGYAAAAAQUIPAAAAAAAUAH70i0ybtASegbOrIeDI; incap_ses_1616_1661977=blD1e9JYLnBG1C5yhy9tFl/PcGYAAAAAVAbwd1t5KN04BlzTbHmXKQ==; _ga_Y0W8DGNBTB=GS1.1.1718668089.1.1.1718669153.0.0.0',
  'priority': 'u=0, i',
  'referer': 'https://engage.metmuseum.org/',
  'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
