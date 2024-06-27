import requests

url = "https://www.metmuseum.org/api/site_search?searchFacet=Videos&page=1"

payload = {}
headers = {
  'accept': '*/*',
  'accept-language': 'es-ES,es;q=0.9',
  'baggage': 'sentry-environment=vercel-production,sentry-release=bb83dcc256a5da5aae902b583ee55ed612e798a8,sentry-public_key=fc26ffe1f7754e9aaa45cbb8fb82b860,sentry-trace_id=12ed83d9f407454cbd54bda1097edfad',
  'cookie': '_gcl_au=1.1.177481860.1719450468; _parsely_session={%22sid%22:1%2C%22surl%22:%22https://www.metmuseum.org/%22%2C%22sref%22:%22%22%2C%22sts%22:1719450469494%2C%22slts%22:0}; _parsely_visitor={%22id%22:%22pid=63a316c8-8038-4ee8-9ac4-ec12a602ac67%22%2C%22session_count%22:1%2C%22last_session_ts%22:1719450469494}; _gid=GA1.2.894875246.1719450470; _tt_enable_cookie=1; _ttp=a1z1zhmXnrYxAWBOmcK7Y3xLbte; QuantumMetricSessionID=813a4caf5ce06c12b9bb20be0b340f2a; QuantumMetricUserID=82de6960966855c5badf112a6be1f814; __qca=P0-1905067046-1719450470359; shell#lang=en; incap_ses_1470_1661922=5+h5WGi4bkwNNdMiS31mFHy7fGYAAAAADQtuy+CU9rj6Z0uLpB4w7w==; __RequestVerificationToken=ixVJBNo7LM75Vz_zAleh--IotEn8vU_AqSEz_qHds66FSmbRTIv9DuXXtlx83EntdbUB4ItQRGACufFExYP6OxxMeyY1; visid_incap_1661922=Uos7cDteQVuFiZOuq8OMWX27fGYAAAAAQUIPAAAAAAA77+6BLoV8GnuUpVX5d4rq; incap_ses_1473_1661922=OrHjfVvDfQHTH/AQxyVxFIe7fGYAAAAAx1q9PQLF9DunO9m/mweMsQ==; incap_ses_1454_1661922=5bcBPqTKTSYlKzTWYKUtFIi7fGYAAAAA2vyoYiDLVIKsF5KP0hPQdQ==; incap_ses_1478_1661922=QXUWXMC6czW3KURJQOmCFIi7fGYAAAAAiw704EUh0KcNkLBxCIAUfA==; incap_ses_784_1661922=lc2+KSBHzhnK0/A5+VPhCom7fGYAAAAAe1SA8Gq9TlXnDtV6LzshOQ==; incap_ses_1474_1661922=xE6MSgpk7GZlF960RbN0FIm7fGYAAAAArzvb7470222QSxWCdQ5Swg==; incap_ses_1242_1661922=K0IEFNCjYVqF7xq2gng8EYm7fGYAAAAAQWyyNy2x2aV60qx8Cm5RvA==; incap_ses_788_1661922=RbC2HmKeNiEhj2vQ7InvCom7fGYAAAAA/hpxBHCFOKmhUX2PURJgqw==; incap_ses_1312_1661922=b2/4ZWIX6ByH/G1wISk1Eom7fGYAAAAAt/5p7FDrJTnhXYR1K24qMA==; incap_ses_1475_1661922=EekNMRZGNE4ME9dZxEB4FIm7fGYAAAAAXye6lBiKFNlkhjvxFiojRg==; incap_ses_1455_1661922=dvgVfcLgySL85nZ63zIxFIm7fGYAAAAACqXuhQiB8AIexxhTy2fHvw==; incap_ses_1298_1661922=z+28XDzWHTwFl7ptNGwDEom7fGYAAAAAXy+bhj8Z5ygwJuDpy4pzKg==; incap_ses_1476_1661922=UxB6QCXmID1USH/+Qs57FIm7fGYAAAAAPMChRqYMaojF/9+A6kMguw==; incap_ses_1693_1661922=zm/AL3QgGTSh3uiqnL5+F4m7fGYAAAAAHVsRe2W1/fCxPFS9hZpwEA==; incap_ses_1472_1661922=iBQoNyLWiSMI3j9sSJhtFI67fGYAAAAAp6Sc10x+XITH4uhPQRq8og==; metNotificationBanner=visited; aceSession=sDN3/rNf2S85K2fMayvV7f3Pd/X5g/mIMBg7NPMAtn53VGkrZg4LKjzP79EaK6K3y2AoF/YzMa+lT68dqYdw+ug473bi4SmRF2C54pshPY7YLcqiIDyeDoB0tAQyAOI0XPxfriAvmDabCoUWAwIJYUfwcHO+mPuDfWPVu9cFU6ReEcENSeXQ2u746D79AecR; nlbi_2349797=h/uEAVsxqw+HX311zMiLaQAAAABgVvX8cumdI0IgOi/jmmU0; visid_incap_2349797=inozJV0bRl2GtSe0HErQKr27fGYAAAAAQUIPAAAAAACrovbwp3EizUnALunlisZG; incap_ses_1730_2349797=7OeCWTesZzgmMfEn6DECGL67fGYAAAAAAqDz1ZOKIXIaBqO19nOY8A==; incap_ses_1241_1661922=JqU+Ldq0fEHa1XMRBOs4Eb67fGYAAAAA42YOXn6bXYGYjzwnyXG2cw==; incap_ses_1477_1661922=gwybBVGTG2bP+VSjwVt/FL67fGYAAAAAEizyrlYeIuuLD8+z/RSAyA==; nlbi_2349797_2147483392=VsUGPfQ8cTFbi+bkzMiLaQAAAACO0k1JOTOpoOt0VI0zBwGj; _ga_80QRY9FZ67=GS1.1.1719450561.1.1.1719450688.0.0.0; _ga_L6ZCHWX6DZ=GS1.1.1719450561.1.1.1719450688.0.0.0; incap_ses_1695_1661922=obTAb0GeC0rvyKDwoNmFF0C8fGYAAAAAxKZTHL1+ENF++0vOqsezeA==; _ga=GA1.2.1632974538.1719450469; _ga_Y0W8DGNBTB=GS1.1.1719450468.1.1.1719450703.0.0.0; incap_ses_1479_1661922=ywPsPVfuxhw6ptLsvnaGFE+8fGYAAAAAXRrkWYmrozLMc8mlkAxFzw==; incap_ses_1696_1661922=mOoMYrfNZjQOhR6ZGGeJF0+8fGYAAAAAmjuNgf/X+pLrsfowhfZIMQ==; incap_ses_1453_1661922=BTkGCrA0yR+XRCAx4hcqFFC8fGYAAAAAd0CoH3efYWEhf12d20rR1w==',
  'priority': 'u=1, i',
  'referer': 'https://www.metmuseum.org/es/search-results?searchFacet=Art',
  'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'sentry-trace': '12ed83d9f407454cbd54bda1097edfad-b25d0d524da0de02',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
