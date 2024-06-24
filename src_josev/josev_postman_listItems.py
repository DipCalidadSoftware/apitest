import requests

url = "https://www.metmuseum.org/api/site_search?q=picture&searchFacet=Primer&page=1"

payload = {}
headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'baggage': 'sentry-environment=vercel-production,sentry-release=4585d0bae0d0d330d9632e07a8bda364a214f2c5,'
             'sentry-public_key=fc26ffe1f7754e9aaa45cbb8fb82b860,sentry-trace_id=8aa9c513e7a54be4b3fead92ad6e4fd2',
  'cookie': 'visid_incap_1662004=Q4jq74afSiaN75vABaEDs9/HcGYAAAAAQUIPAAAAAAB1UsvZFruEfi0VzLx86mig;'
            ' incap_ses_1731_1662004=K7ZBJEtzbkZKAkN6ZL8FGN/HcGYAAAAAnlCfQ+5kvqrKLA6E10cYGA==;'
            ' _gcl_au=1.1.23451007.1718667641; _gid=GA1.2.388701358.1718667641; _tt_enable_cookie=1;'
            ' _ttp=WfY3_qGA8YIM1LYF48BDr3XA1Q3; __qca=P0-738042885-1718667641743;'
            ' QuantumMetricUserID=d1e65c1cd5e5d3a88618bfcdaea8cec3; shell#lang=en;'
            ' __RequestVerificationToken=dRGBR8kQ1PM15zqSKnInu10y-InndZtaHgRrhLCdcuiFGt5bc7aGaKIWhb5BElV3pa8YgEyeCD'
            'nbqDl-cMwy2z0QQlk1; visid_incap_1661922=QvAQMSPKSEi+GqiZpFRxO4fJcGYAAAAAQUIPAAAAAAAtlEbtUPeGC4xFJF/sdB9Y;'
            ' NEXT_LOCALE=en; visid_incap_1661977=h0JVve3fReKnwUwZ4a9b9g3McGYAAAAAQUIPAAAAAADzhc9YN8TiKI+dmkPj8kvJ;'
            ' incap_ses_785_1661922=/WaeBGLZLCc7PKzlcOHkCg3McGYAAAAAAh3MSmAugD7QP7ipeDZxmQ==;'
            ' incap_ses_1731_1661977=Dqm6DeZaMi9Bz0d6ZL8FGA7McGYAAAAA9RvMQBoe9JMdtVx8IWK6DQ==;'
            ' incap_ses_1695_1661922=9Sc+XLquYH4zH36gntmFF4TScGYAAAAA1xLWwWR1o4QcMdqD4yNEJQ==;'
            ' incap_ses_1452_1661922=n6XUB0eLrDj4TNc7YYomFEjTcGYAAAAA24GwxjKXHvPBYnul5dKXfQ==;'
            ' incap_ses_784_1661922=dagGMV3g8HAKn8/p9lPhCkjTcGYAAAAAPAtYPRzmDvBwFTLCNJf9YA==;'
            ' ethn=6/17/2024 8:22:37 PM; incap_ses_789_1661922=lpSHBhqDlXNahRfVZhfzCk7TcGYAAAAAo0GD4ITT8nB02ivqNF3QOQ==;'
            ' incap_ses_1476_1661922=IRW+K+IUXgnkphqwQM57FE7TcGYAAAAA7K6kw4bbetAT/Z6t1mYe4A==;'
            ' incap_ses_1696_1661922=46z0Rvy4/QAUBCNJFmeJF03TcGYAAAAAduRUi2D23K4Vqm4/kHvD2Q==;'
            ' incap_ses_1454_1661922=cmJNSwA6p0g+uTaGXqUtFE7TcGYAAAAADiLw1Ui4pC1EXwIkTIx6MQ==;'
            ' incap_ses_1354_1661922=l4vyWDEnbXYMNk8q5l/KEk3TcGYAAAAAQASw1uUyGsyujUD7jTQ89w==;'
            ' incap_ses_1240_1661922=Z6GbC41SUgpcinQeg101EU7TcGYAAAAAwAO9JOM7VFXeIHH4tg//2A==;'
            ' incap_ses_1472_1661922=kxaeG/zkGTqcHB8cRphtFE/TcGYAAAAA8y5RaLR77iqhNr7/69nEjg==;'
            ' QuantumMetricSessionID=d656e5ab9b3605513a1918707d8f338b;'
            ' incap_ses_1479_1661922=Z/WxHwns7FjKXAqevHaGFEtccmYAAAAAOQSq3kysSGH3wzPFDrpNXg==;'
            ' _parsely_session={%22sid%22:4%2C%22surl%22:%22https://www.metmuseum.org/press/news/2015/'
            'met-museum-presents%22%2C%22sref%22:%22https://www.metmuseum.org/search-results?q=Arte+mad%25C3%'
            '25AD&searchFacet=Press%22%2C%22sts%22:1718770767712%2C%22slts%22:1718690913376};'
            ' _parsely_visitor={%22id%22:%22pid=8f9eccb8-371f-4334-b44b-3d205950c351%22%2C%22session_count%22:'
            '4%2C%22last_session_ts%22:1718770767712}; _uetsid=1fcd19e02df311efa335b1cdca64b306;'
            ' _uetvid=1fcd5ab02df311ef96ae9d8a31691061; _ga_DWPJYPP88X=GS1.2.1718770770.1.0.1718770771.59.0.0;'
            ' xdibx=N4Ig-mBGAeDGCuAnRIBcoAOGAuBnNAjAOwEAcRRADBQMwEAspANCBgG6wB22hLu-qYmQrUidRi3a4uPQS0RIANmhAALbN'
            'gy5UAeh0B3QwDoAtgFNsJ-LjPwTRgPaIA5jpAtFSlToD88S2C4DkiwZgC8JgCGAJacVjZ2AGT-JmDmACbRdhEW8bb2Ts7JAbCRJh'
            'gxzpxh2A4YnJFsALS42JHY0bDuIIp4hCTkVLQMpAC-LBAwGIhmbGig6ZEAngIA2kKDonQAbACcALrj4FDQs2bcAsBHk3DR6So0lA'
            'BMT7v0lGZNAGaU9ACsTXo6Vg2yakS-kU-f229CeZiIf1hNCe6SaGxEFAYu1IIFGQA__; __zlcmid=1MLmnzWVTIwM1Ta;'
            ' _ga_BB83TXR9NF=GS1.1.1718770770.1.0.1718770775.55.0.0;'
            ' incap_ses_1298_1661922=AzRnJXjpfmHnWAQfMmwDElRccmYAAAAA02KDEipGTC6dGtNgaM6G2Q==;'
            ' incap_ses_298_1661922=xfI2L0Ar2XK99tDLgLUiBFRccmYAAAAA4Czhy6XeWIS6KsspJYaUyQ==;'
            ' incap_ses_1471_1661922=AMrrA4I4hxRxy594xwpqFF9ccmYAAAAAdKngJzRptW89z41l+7urTQ==;'
            ' incap_ses_1473_1661922=H4jEebIo2wi7VMPBxCVxFF9ccmYAAAAANfDyBm7g6MFc4Lmc7vKKFg==;'
            ' incap_ses_1693_1661922=v/FxUgVjYm88m8xcmr5+F19ccmYAAAAAZddT1hrmaeBXqnJVB+yKfA==;'
            ' incap_ses_787_1661922=6JErL8CJjHtniEnca/zrCmBccmYAAAAANSz6slVYU+7l4D/5SCZssA==;'
            ' _hjSession_3360071=eyJpZCI6ImI0MWRjODdhLTllNTUtNDllYi04MWY2LTE2NDBiNzFiOTk0NyIsImMiOjE3MTg3NzA'
            '3ODkwNDUsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MX0=;'
            ' incap_ses_1477_1661922=MggoS9SJKx81HYZUv1t/FGBccmYAAAAA5EWoB9FyCp3YfU1MJJjBHg==;'
            ' incap_ses_1239_1661922=2Z8BLK53QCE+CZ4lAtAxEWlccmYAAAAAEMrY12pLJFED6svXXQneZQ==;'
            ' incap_ses_1455_1661922=ne0TYhY7ZQI6Fooq3TIxFGlccmYAAAAA4buz1vo3JR+AUzTumbYYiQ==;'
            ' incap_ses_1241_1661922=paBxGvSGxxiUMCzCAes4EWpccmYAAAAAbVpRxnpGC8eg5NxtpRAQFw==;'
            ' incap_ses_1474_1661922=pObsC7FZkmQHJmJmQ7N0FGlccmYAAAAAjkPn2x4g6Xwarb0ikRp8ig==;'
            ' incap_ses_1694_1661922=bBVwIoWi/Q0NUnYAGUyCF2tccmYAAAAAVQ8Xlljxk+Ycq0HmPBl/hA==;'
            ' _hjSessionUser_3360071=eyJpZCI6IjcyOWJmZTA3LTE0ZjYtNTBhYy05MDYzLTUzMTdjNGI5NGNiYSIsImNyZWF0ZWQiOjE3M'
            'Tg3NzA3ODkwNDQsImV4aXN0aW5nIjp0cnVlfQ==; incap_ses_786_1661922=DWtENgQRqhMCCmU37W7oCpNccmYAAAAAN2EjC0'
            '9wIH45Y+hYdMgIgA==; incap_ses_1478_1661922=7Jffe67xFRTE3kT7PemCFEhicmYAAAAAvimFaQ3pP1woJjpvcOknJA==;'
            ' incap_ses_1698_1661922=AB5yWgi+71GbWX2TE4KQF0licmYAAAAAahGnjW8nLYmWHQ7OHeFOVg==; incap_ses_297_166'
            '1922=9w3metlDz1Rm+P0mAigfBF5jcmYAAAAAOv6yMxfE50CAByI3oV9+Aw==; incap_ses_1722_1661977=+Wc1N7ja7EvxRa'
            'es98XlFxplcmYAAAAAsH5NPVbM1NQXyWwluYqsjw==;'
            ' incap_ses_1475_1661922=SmWATYaXnR6HwwsLwkB4FBplcmYAAAAAVN+TXg8PMvQMBvEl49dAWA==;'
            ' _ga_Y0W8DGNBTB=GS1.1.1718770767.3.1.1718773042.0.0.0; _ga=GA1.2.684403000.1718667641',
  'priority': 'u=1, i',
  'referer': 'https://www.metmuseum.org/search-results?q=picture',
  'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'sentry-trace': '8aa9c513e7a54be4b3fead92ad6e4fd2-871f9cf164e21654',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                '125.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
