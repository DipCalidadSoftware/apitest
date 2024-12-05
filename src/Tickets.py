import requests

url = "https://engage.metmuseum.org/api/productioneventapi/events?productionSeasonIds=728092&performancestartdate=2024-06-19T21:07:24.321Z&performanceenddate=2024-08-01T21:07:24.321Z&mos=69"

payload = {}
headers = {
  'Accept': '*/*',
  'Accept-Language': 'es-419,es;q=0.9',
  'Connection': 'keep-alive',
  'Cookie': 'visid_incap_1662004=/f+VAVlqTnWLKGOy0AcqlhPIcGYAAAAAQUIPAAAAAADz0K1szFp6h0+kOR/x0jSS; incap_ses_545_1662004=6xsIF8vk8yA3NGcYtDqQBxPIcGYAAAAAuWlfdiaAWx2CQ/YTH1PtLg==; _gcl_au=1.1.923939922.1718668613; _tt_enable_cookie=1; _ttp=GTo7gFVR7Pk7087dQ-uAfYukKm3; __qca=P0-952754689-1718668613177; QuantumMetricUserID=edc1cb844bf8b4c605374bd0351259d5; visid_incap_1661922=hzxgYuY/T++79mpozKEYlmzOcGYAAAAAQUIPAAAAAABeAyf4c/e5GlYIvPt8h8gd; visid_incap_1661977=H+EuIT20TAO87ZospnWSi3fOcGYAAAAAQUIPAAAAAADbybOWx8HQt0jVG5kppNKo; QuantumMetricSessionID=c7fe96f86b8a1b4e6d9758b1fdbc26e1; _parsely_session={%22sid%22:2%2C%22surl%22:%22https://www.metmuseum.org/es/search-results?q=sunflowers%22%2C%22sref%22:%22https://www.metmuseum.org/es%22%2C%22sts%22:1718829486728%2C%22slts%22:1718668613141}; _parsely_visitor={%22id%22:%22pid=16cff65a-3f1e-4eda-9067-960109883046%22%2C%22session_count%22:2%2C%22last_session_ts%22:1718829486728}; incap_ses_1241_1661922=0akuKQgxpRpzcbjCAes4ET1Cc2YAAAAAXVlkUXHrePDLmy0oz89z1w==; incap_ses_8073_1661922=hNeJbAyEumGs/LmI0Q4JcD1Cc2YAAAAAqyt4qz/+Rgcd5LTdpRKAAQ==; incap_ses_1474_1661922=/xR5NZsuTWqqixBnQ7N0FH9Cc2YAAAAAm9e7NxRg5nGfOUlwd2Xcyg==; _gid=GA1.2.779536190.1718830556; incap_ses_1694_1661922=bYHDIbLEvARslSIBGUyCF+FFc2YAAAAAywY2nZLhI2C/Bpxy3tVYGQ==; incap_ses_545_1661977=h4VQQiu133i1UT4atDqQB+FFc2YAAAAA1iHfEg2DfCVmMsU32wUogQ==; incap_ses_1477_1661922=FEWOfBIJth9YTDVVv1t/FC1Gc2YAAAAAOQOr75596bO0QTG0Ze4Tlw==; aceSession=VCfT2J1QG/khKKnnvvlFoRjh8H5sNCKpumm014WuL5Wecwfd2v1hDlLWE/14oVz4ATsRDTO2Qca3sGlvBJQzNyHIblpvJjbsKcYgOwn4NfXkMVMSn7hSgheMXD7G/w51b5E9gTUTBR+8dnbOrYWGxyC6kYqiooo0ewRJw7D3RC1SoIJr7Cf6z8lwx3RwaPnh; personalisationGroupsNumberOfVisits=1; personalisationGroupsNumberOfVisitsSessionStarted=1; personalisationGroupsPagesViewed=1621; nlbi_2349797=x2qdSmEYEUv7D57bzMiLaQAAAABS5I74q9ExGokMejIQKf3u; visid_incap_2349797=tEyAKdDHRDer+DjIS4qiZn1Ic2YAAAAAQUIPAAAAAAATmJ+Po0wEh/cEw/PDfyUH; incap_ses_545_2349797=zTNxJwQjSkZLwkAatDqQB35Ic2YAAAAACSn+m41REXakrm6LBaQWRw==; _dc_gtm_UA-72292701-1=1; _ga=GA1.1.1371690355.1718668613; _ga_80QRY9FZ67=GS1.1.1718831232.1.0.1718831232.0.0.0; _ga_Y0W8DGNBTB=GS1.1.1718829629.2.1.1718831232.0.0.0; incap_ses_1697_1661922=aY9nPtmJJwJFAnbvlPSMF4BIc2YAAAAAcXFkMJ7+ot0VQygYzYjE4g==; incap_ses_1312_1661922=KhlRO2FXGghIoIUhHyk1EoBIc2YAAAAA0TfyeTMnB+f7kWWS3dZ11A==; incap_ses_1298_1661922=fztxQWmcR0tmzaQfMmwDEoFIc2YAAAAAbAVif8DCwYdBJ3tOj8JhJA==; nlbi_2349797_2147483392=ucqOSRHKIwz5FnbszMiLaQAAAABmE0Xm8ib8gRTVS/ydfQNR; reese84=3:Z7IxllHrNqS1jcB4znV5HA==:gGybn1z6qiUkXAQqdz84JOaD3f2FZ2EGaQZ16O/OQ1oWZCiRMk3VXheuGQrSxqmckfr2fuGxQVLHA+qSTTtTA647vWQBsZyzV8/knz5rWqu1QV6iOvIHfcY3XB7JU+ECjk9YySlVD8NZbwo4epnsQhBLZ/TOsbnlHnF5IrFb3H6480eivqJT/btzB1WCv76NSg64d7O2onTk8FcmuAYOAsR3sWPH/g69nb7GhBoXL+lFryo+viMS27Qan3ZKjOgwy9xWPn6CJmiuouRe06hR1sPP6XSU6/lcWSlmRx+POMV8UHKAdz2+bDqe6hb7I5LMbbOiXnb5cZAGg0V2s6P14LUX8tEiFEJZ/eYBkWITRMVXypR1oVwZB4kHz8Qx+31degEnfYBIIOSIdQ/LOGhQwxJCYS4sIC0U+xQm9ml9qtotBJUmRiXoelKKJofNhNwVszxZ7ZKo4zaXOpNPmDYe7Q==:xuYjjNMf4h6kdj8WGCt4yHtWTG1d7n7P32B+L3cItdI=; _ga_L6ZCHWX6DZ=GS1.1.1718831232.1.0.1718831236.0.0.0; aceSession=zRbkiyxuvn9PcXqUrzEcZCu/uMHlCMXg7Wswe89TwO5axj0BDlwnIV8WuFXpTiHytLYT/r+wphSke371uwMPB09SLp73JzE+X79vPBqXQyXWZyqfwsxTAWSYu9Usj8A1N67KlpiaON1B0LRLSmCMvF8j2Fwadk1Fug2A0D8RtQuIzNu4RJ9GN6RmkXeBdT+x; incap_ses_545_1662004=FcA/f40BVExiNT8atDqQB9dGc2YAAAAAl7g8Q5OX2guK2f9dc6lKwA==; visid_incap_1662004=M2opLTipR0KHFoTvKohXYh7OcGYAAAAAQUIPAAAAAAC+ShrzCsjRRySGgAgX28Ib',
  'Referer': 'https://engage.metmuseum.org/admission',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
  'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
