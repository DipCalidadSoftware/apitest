import requests

url = "https://store.metmuseum.org/checkout/sidebar/updateItemQty/?cartQtyUpdate=true"

payload = "item_id=15104492&item_qty=1&form_key=O2X5P7GX1FgKw4Ih"
headers = {
  'accept': 'application/json, text/javascript, */*; q=0.01',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'cookie': 'visid_incap_1662004=Q4jq74afSiaN75vABaEDs9/HcGYAAAAAQUIPAAAAAAB1UsvZFruEfi0VzLx86mig;'
            ' incap_ses_1731_1662004=K7ZBJEtzbkZKAkN6ZL8FGN/HcGYAAAAAnlCfQ+5kvqrKLA6E10cYGA==;'
            ' _gcl_au=1.1.23451007.1718667641; _gid=GA1.2.388701358.1718667641; _tt_enable_cookie=1;'
            ' _ttp=WfY3_qGA8YIM1LYF48BDr3XA1Q3; __qca=P0-738042885-1718667641743;'
            ' QuantumMetricUserID=d1e65c1cd5e5d3a88618bfcdaea8cec3;'
            ' visid_incap_1661922=QvAQMSPKSEi+GqiZpFRxO4fJcGYAAAAAQUIPAAAAAAAtlEbtUPeGC4xFJF/sdB9Y;'
            ' visid_incap_1661977=h0JVve3fReKnwUwZ4a9b9g3McGYAAAAAQUIPAAAAAADzhc9YN8TiKI+dmkPj8kvJ;'
            ' incap_ses_1731_1661977=Dqm6DeZaMi9Bz0d6ZL8FGA7McGYAAAAA9RvMQBoe9JMdtVx8IWK6DQ==;'
            ' incap_ses_1695_1661922=9Sc+XLquYH4zH36gntmFF4TScGYAAAAA1xLWwWR1o4QcMdqD4yNEJQ==;'
            ' incap_ses_1452_1661922=n6XUB0eLrDj4TNc7YYomFEjTcGYAAAAA24GwxjKXHvPBYnul5dKXfQ==;'
            ' incap_ses_784_1661922=dagGMV3g8HAKn8/p9lPhCkjTcGYAAAAAPAtYPRzmDvBwFTLCNJf9YA==;'
            ' incap_ses_789_1661922=lpSHBhqDlXNahRfVZhfzCk7TcGYAAAAAo0GD4ITT8nB02ivqNF3QOQ==;'
            ' incap_ses_1476_1661922=IRW+K+IUXgnkphqwQM57FE7TcGYAAAAA7K6kw4bbetAT/Z6t1mYe4A==;'
            ' incap_ses_1696_1661922=46z0Rvy4/QAUBCNJFmeJF03TcGYAAAAAduRUi2D23K4Vqm4/kHvD2Q==;'
            ' incap_ses_1454_1661922=cmJNSwA6p0g+uTaGXqUtFE7TcGYAAAAADiLw1Ui4pC1EXwIkTIx6MQ==;'
            ' incap_ses_1354_1661922=l4vyWDEnbXYMNk8q5l/KEk3TcGYAAAAAQASw1uUyGsyujUD7jTQ89w==;'
            ' incap_ses_1240_1661922=Z6GbC41SUgpcinQeg101EU7TcGYAAAAAwAO9JOM7VFXeIHH4tg//2A==;'
            ' incap_ses_1472_1661922=kxaeG/zkGTqcHB8cRphtFE/TcGYAAAAA8y5RaLR77iqhNr7/69nEjg==;'
            ' QuantumMetricSessionID=d656e5ab9b3605513a1918707d8f338b;'
            ' _parsely_session={%22sid%22:4%2C%22surl%22:%22'
            'https://www.metmuseum.org/press/news/2015/met-museum-presents%22%2C%22sref%22:%22'
            'https://www.metmuseum.org/search-results?q=Arte+mad%25C3%25AD&searchFacet='
            'Press%22%2C%22sts%22:1718770767712%2C%22slts%22:1718690913376}; _parsely_visitor={'
            '%22id%22:%22pid=8f9eccb8-371f-4334-b44b-3d205950c351%22%2C%22session_count%22:4%2C%22last_session_ts%'
            '22:1718770767712}; PHPSESSID=44e610f5ec0ced690f5b7c094ad86bb4; form_key=O2X5P7GX1FgKw4Ih;'
            ' mage-banners-cache-storage={}; mage-cache-sessid=true; mage-messages=;'
            ' _mibhv=anon-1718770770415-3365245546_7119;'
            ' form_key=O2X5P7GX1FgKw4Ih; __zlcmid=1MLmnzWVTIwM1Ta;'
            ' incap_ses_1298_1661922=AzRnJXjpfmHnWAQfMmwDElRccmYAAAAA02KDEipGTC6dGtNgaM6G2Q==;'
            ' incap_ses_298_1661922=xfI2L0Ar2XK99tDLgLUiBFRccmYAAAAA4Czhy6XeWIS6KsspJYaUyQ==;'
            ' incap_ses_1471_1661922=AMrrA4I4hxRxy594xwpqFF9ccmYAAAAAdKngJzRptW89z41l+7urTQ==;'
            ' incap_ses_1693_1661922=v/FxUgVjYm88m8xcmr5+F19ccmYAAAAAZddT1hrmaeBXqnJVB+yKfA==;'
            ' incap_ses_1477_1661922=MggoS9SJKx81HYZUv1t/FGBccmYAAAAA5EWoB9FyCp3YfU1MJJjBHg==;'
            ' incap_ses_1474_1661922=pObsC7FZkmQHJmJmQ7N0FGlccmYAAAAAjkPn2x4g6Xwarb0ikRp8ig==;'
            ' incap_ses_1694_1661922=bBVwIoWi/Q0NUnYAGUyCF2tccmYAAAAAVQ8Xlljxk+Ycq0HmPBl/hA==;'
            ' _hjSessionUser_3360071=eyJpZCI6IjcyOWJmZTA3LTE0ZjYtNTBhYy05MDYzLTUzMTdjNGI5NGNiY'
            'SIsImNyZWF0ZWQiOjE3MTg3NzA3ODkwNDQsImV4aXN0aW5nIjp0cnVlfQ==;'
            ' incap_ses_786_1661922=DWtENgQRqhMCCmU37W7oCpNccmYAAAAAN2EjC09wIH45Y+hYdMgIgA==;'
            ' incap_ses_1698_1661922=AB5yWgi+71GbWX2TE4KQF0licmYAAAAAahGnjW8nLYmWHQ7OHeFOVg==;'
            ' incap_ses_297_1661922=9w3metlDz1Rm+P0mAigfBF5jcmYAAAAAOv6yMxfE50CAByI3oV9+Aw==;'
            ' incap_ses_1722_1661977=+Wc1N7ja7EvxRaes98XlFxplcmYAAAAAsH5NPVbM1NQXyWwluYqsjw==;'
            ' incap_ses_1475_1661922=SmWATYaXnR6HwwsLwkB4FBplcmYAAAAAVN+TXg8PMvQMBvEl49dAWA==;'
            ' incap_ses_1478_1661922=RVWQT2kPdTz4Jkf7PemCFMRmcmYAAAAA/u8YkJ+2VBgvqFr+LOwvWw==;'
            ' incap_ses_787_1661922=64qcSIxQqmhvgkzca/zrCsRmcmYAAAAA8ZCIQ7v+RiccsAXto4/N9w==;'
            ' incap_ses_1241_1661922=CNRfYAoNN3NyQS/CAes4EcRmcmYAAAAAxi7Pnih3hu/acrgKnMk7Uw==;'
            ' incap_ses_1239_1661922=cDmoGxUOFCLb1qAlAtAxEcRmcmYAAAAAPf3rWZWTuv+Xf7v5l6Lx8g==;'
            ' incap_ses_1479_1661922=oe/9BtTc/Vmdsg6evHaGFMVmcmYAAAAATkgTdQOLuRYDD+Gduhzmkw==;'
            ' incap_ses_1473_1661922=F0syCfsZhnK8qsbBxCVxFMVmcmYAAAAAE9PVbGTq9zBtfCM5FhpJYA==;'
            ' incap_ses_785_1661922=auUnGXY7C3xmNp3mcOHkCpRocmYAAAAA65rQFs6q8I74LO7aJF3RTg==;'
            ' incap_ses_1455_1661922=fiFQS1afiDNCd40q3TIxFC9pcmYAAAAAaoewKO3JsGcZGtNVl/GMhQ==;'
            ' oscw_close_policy=IYIwxkA_; oscw_close_policy_ext=B4TwXkA_;'
            ' klevu_cat_klevu_164268060165713861=All%20Kids%3B%3BAges%203-4%3B%3BKids\'%20Books%3B%3BAll%20Books%3B%'
            '3BImpressionism%3B%3BThe%20Met%20Store%20Gift%20Finder; klevu_rcp_klevu_164268060165713861=MTE3NzM=;'
            ' yotpo_pixel=ee303479-1a9e-4719-89be-b7345c98053f;'
            ' _sp_id.88ed=f380f9f2dd412236.1718774165.1.1718774165.1718774165;'
            ' _sp_ses.88ed=*; private_content_version=3c6730c9f048cdfa4a07e86d6d49bfd5;'
            ' _gat_UA-1266565-1=1; klv_mage={"expire_sections":{"customerData":1718775469}};'
            ' _ga=GA1.2.684403000.1718667641; _gat_UA-1266565-7=1; mage-cache-storage={};'
            ' mage-cache-storage-section-invalidation={}; _uetsid=1fcd19e02df311efa335b1cdca64b306;'
            ' _uetvid=1fcd5ab02df311ef96ae9d8a31691061; recently_viewed_product={};'
            ' recently_viewed_product_previous={}; recently_compared_product={};'
            ' recently_compared_product_previous={}; product_data_storage={};'
            ' xdibx=N4Ig-mBGAeDGCuAnRIBcoAOGAuBnNAjAOwEAcRRALOQMwBspADADQgYBusAdtmgKytc-VMTIVKBRnQCclaaw65uvVJVaI'
            'kAGzQgAFtmwZcqAPQmA7pYB0AWwCm2G.Fx34NqwHtEAcxMhWmlo6JgD88I5guB5IsHYAvDYAhgCWXE4ubgBk4TZg9gAmyW4JDumu'
            '7l7e2RGwiTYYKd5ccdgeGFyJ7AC0uNiJ2Mmw.iCaeIQk5FSSMnIAvqwQMBiIduxooPmJAJ7CANqik4wUNAQyALrz4FDQq3Y8wqAA'
            'TIzU0nTrIGvoIEMirCr7CbiAgEaR8AiUC6CD6.FggAFQkAob6w.5oXaI.IwtBwhGXX6gX4ENGoQFiKYSN50C6XZ5yAg0D5fQmEEl'
            'kyYSIiMGiPAiIh4.HFsxHIlmoXHozHY8XC.HS4nw9EHcTPMigmmXRZwZJY1AgGiMR6PWSMOxdABmLz4XUo-VgdC6iXNiTNfDolEe'
            'diIfA9PPyXWVXIoEOkpBAsyAA__; section_data_ids={%22customer%22:1718774868%2C%22compare-products%'
            '22:1718774868%2C%22last-ordered-items%22:1718774868%2C%22cart%22:1718774868%2C%22directory-data%22'
            ':1718774868%2C%22captcha%22:1718774868%2C%22wishlist%22:1718774868%2C%22instant-purchase%22:1718774'
            '868%2C%22loggedAsCustomer%22:1718774868%2C%22multiplewishlist%22:1718774868%2C%22persistent%'
            '22:1718774868%2C%22review%22:1718774868%2C%22ammessages%22:1718774868%2C%22recently_viewed_product%'
            '22:1718774868%2C%22recently_compared_product%22:1718774868%2C%22product_data_storage%22:1718774868%'
            '2C%22paypal-billing-agreement%22:1718774868}; _ga_Y0W8DGNBTB=GS1.1.1718770767.3.1.1718774880.0.0.0;'
            ' _ga_BB83TXR9NF=GS1.1.1718774105.2.1.1718774880.47.0.0;'
            ' _ga_DWPJYPP88X=GS1.2.1718774105.2.1.1718774880.51.0.0;'
            ' PHPSESSID=44e610f5ec0ced690f5b7c094ad86bb4; form_key=O2X5P7GX1FgKw4Ih;'
            ' private_content_version=82aca700e6f2c3f90cb6fb7babdbc6ce',
  'origin': 'https://store.metmuseum.org',
  'priority': 'u=1, i',
  'referer': 'https://store.metmuseum.org/checkout/cart/',
  'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                '125.0.0.0 Safari/537.36',
  'x-newrelic-id': 'VQEBWFBSCxAHXVlUAgYHUA==',
  'x-requested-with': 'XMLHttpRequest'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
