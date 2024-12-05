import http.client

conn = http.client.HTTPSConnection("www.metmuseum.org")
payload = ''
headers = {
  'accept': '*/*',
  'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8',
  'baggage': 'sentry-environment=vercel-production,sentry-release=f0734f7c471e368fffd36bfdd8490a0ae7a7e22f,sentry-public_key=fc26ffe1f7754e9aaa45cbb8fb82b860,sentry-trace_id=f0495f2ac29841bda822af46383de10b',
  'cookie': 'NEXT_LOCALE=en; _gcl_au=1.1.416405801.1719249175; _gid=GA1.2.1922947038.1719249175; _parsely_session={%22sid%22:1%2C%22surl%22:%22https://www.metmuseum.org/%22%2C%22sref%22:%22https://metmuseum.github.io/%22%2C%22sts%22:1719249175017%2C%22slts%22:0}; _parsely_visitor={%22id%22:%22pid=cf89bf8f-45da-48a8-a15a-2189c28409ac%22%2C%22session_count%22:1%2C%22last_session_ts%22:1719249175017}; _fbp=fb.1.1719249175100.845494370227328104; _tt_enable_cookie=1; _ttp=86OlJ154-KBX-ADjY0OGKL8AsKm; __qca=P0-833869897-1719249175240; QuantumMetricSessionID=60d5250fb90a9852d6be27d5b65ce07f; QuantumMetricUserID=fef9fe4cf781b5c3d445aa4584e63f9e; incap_ses_1693_1661922=TUPUC517bmTQbKVimr5+F2CpeWYAAAAAywQRD4ENLIEJzQuGQcPW6Q==; incap_ses_1471_1661922=N1dSabBNfRonc2fFyQpqFGGpeWYAAAAA1PDe5aNhWkVrsgPB3nsWOA==; visid_incap_1661922=tZ9yVW1QT6uD90mL6njDT2GpeWYAAAAAQUIPAAAAAAAuOoOccm0LunwPPrn47e/x; incap_ses_1354_1661922=aFP0I7C7jxmT/Xl36F/KEmGpeWYAAAAARMFCNKsc0SIsoCWjpFFq8A==; shell#lang=en; __RequestVerificationToken=Qpe1UiuHnjnSzo-ribJqADCiX5FRBEIjfiMGo7YruCG65pnMV0pOXoin5knN22A79nSeAQRUzJ1IZIvgUQFIAXWabO81; incap_ses_1470_1661922=GIcmVg6d5zV3u6IgS31mFHepeWYAAAAAEi/VGRaHgBz52D2H1h64tA==; incap_ses_1453_1661922=xuhtG1owMyzjnl0v4hcqFHepeWYAAAAAQ2H5NJiNWwuFNexSnX89ug==; incap_ses_1241_1661922=k+7QXARBKwwtNKMPBOs4EXipeWYAAAAAmSwoU4wvLRH3cu/kKg/EMw==; incap_ses_785_1661922=FbnEUoXAGExaSuPqcOHkCnepeWYAAAAAQBurD0TM90mP5Sc6eH0sdw==; incap_ses_1475_1661922=tuICFhi42QAVMzgQwkB4FHipeWYAAAAAHLO1R8c/9Kgjnv3AZwtNWA==; incap_ses_1696_1661922=9U6FaIE5zyNCO4pPFmeJF3epeWYAAAAAybM3vV5hay7NzfrKLrVsAg==; incap_ses_786_1661922=uKyRUGUpUwxd1Es77W7oCnipeWYAAAAAfhEQpz1Lrn4q0jmn6KjPOQ==; incap_ses_1473_1661922=ZYgZRxEDvWu1Ue8OxyVxFHipeWYAAAAAZsTz2LIhui+hnNnIET7ZkA==; incap_ses_784_1661922=SABxTFSJFgvuiiTw9lPhCnipeWYAAAAAl5KWQF1yNxUHDXKLDLpmyw==; incap_ses_787_1661922=JBiAI4rHq3UAEobga/zrCnmpeWYAAAAAvlZX+E4rIJ4VcZujQ+ayYg==; incap_ses_297_1661922=qFutdlL+VV/qWPZ1BCgfBHipeWYAAAAAkxNkA3U7QAwzIszkbjibiQ==; incap_ses_1472_1661922=x+SMA/R40Wt1Zi9qSJhtFH6peWYAAAAAQvk5i/sefZWR9Yzb9s8vlQ==; incap_ses_1474_1661922=6LZMIE+AcmkKcVdrQ7N0FH+peWYAAAAAmM+9d8xWlT8Yg19lJoXtog==; incap_ses_1298_1661922=8bFZbWRYSWBoR+trNGwDEoCpeWYAAAAALJY2kGxb5OzWLwcoeoVqvA==; incap_ses_1452_1661922=LQzoAS2g7hQO4ZmKY4omFH+peWYAAAAAmbfr/O7+8zd9ivF7O/cvYA==; incap_ses_789_1661922=JeEDJBeKpCf/4AYkaRfzCoipeWYAAAAAB4V6BD1BGwj8cFEme0rV6Q==; incap_ses_298_1661922=rmIXGWmL0UgaTKQYg7UiBImpeWYAAAAAHLPUmzqYx2R0CqD/d0vbBQ==; incap_ses_1479_1661922=85XxYitmpkMU4SajvHaGFImpeWYAAAAAhpbHbh93TAWPhHjUiJ1gWA==; incap_ses_1239_1661922=2FSsAP2zXF2KkZ50BNAxEYmpeWYAAAAAoiqIfU+zCdBfOryD3auQlQ==; incap_ses_1478_1661922=QZFFZt6KH1Q1lUUCPumCFImpeWYAAAAAr+GLx9AeNqTfetFObBhskQ==; incap_ses_1694_1661922=exsCLDVwukHFTHkGGUyCF4ypeWYAAAAAzXZgkv8f/C3uVPlHd0KO6g==; incap_ses_1454_1661922=EAHHXbr5tEeU/D/UYKUtFJKpeWYAAAAADLAYAz0FTnZj2Dnr5Y3HUg==; incap_ses_788_1661922=kBphaxsYgVdrGemJ6onvCpipeWYAAAAAQnIqrV1kgUApNlsszW9CyQ==; incap_ses_1254_1661922=eH0ZN0QTw2091PptchpnEZipeWYAAAAA5QPvRFbfbw+ri+zY9Zv6/Q==; incap_ses_1312_1661922=SMHzKm+F/C4sA5xuISk1EpmpeWYAAAAAPn4lHsMWz7gBdi9ghqkZ8Q==; incap_ses_1695_1661922=DhX9TEJo0H4gr+ymntmFF5mpeWYAAAAAv7e6KC10U7CLKhoAbxpgRQ==; incap_ses_1697_1661922=lKvRaxXNEXgxIN/zlPSMF9OpeWYAAAAAKQ9OtznfoCcOH+ieQmvOzQ==; _ga_Y0W8DGNBTB=GS1.1.1719249174.1.1.1719249579.0.0.0; _ga=GA1.2.965834513.1719249175; _gat_UA-72292701-1=1',
  'priority': 'u=1, i',
  'referer': 'https://www.metmuseum.org/search-results?',
  'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'sentry-trace': 'f0495f2ac29841bda822af46383de10b-a9d63c2723e4adf5',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
}
conn.request("GET", "/api/site_search?searchFacet=MetMedia&page=1", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))