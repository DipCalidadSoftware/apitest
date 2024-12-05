import requests

url = "https://www.metmuseum.org/about-the-met/collection-areas"

payload = {}
headers = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'en-US,en;q=0.9,es;q=0.8',
  'cache-control': 'no-cache',
  'cookie': '_gcl_au=1.1.2033022923.1718822122; _gid=GA1.2.1037850266.1718822122; _parsely_session={%22sid%22:1%2C%22surl%22:%22https://www.metmuseum.org/%22%2C%22sref%22:%22%22%2C%22sts%22:1718822122381%2C%22slts%22:0}; _parsely_visitor={%22id%22:%22pid=7945c643-a495-4832-956d-4254e3bd34e0%22%2C%22session_count%22:1%2C%22last_session_ts%22:1718822122381}; _tt_enable_cookie=1; _ttp=3y9QOgdXcgw6X1OiRiZlR1kC4dC; _fbp=fb.1.1718822122898.448311044487312979; __qca=P0-1660362713-1718822122630; QuantumMetricSessionID=ac8426844bdefa83062cae733681752e; QuantumMetricUserID=fb64bbf959822cd92cf09d099f20b9e5; shell#lang=en; __RequestVerificationToken=LzmgysRi8OwzVT1Z1d2_t4AYNUSQb4Mxa-1yNRYko5S1kRFNMLssQS1H24rFRzMT9HVBEUB11TTwPTC53LQ5p9o2X301; visid_incap_1661922=hSfe4FTdRbyfg4rd6OdfcQElc2YAAAAAQUIPAAAAAAC55xFUY4TVPX9B4DNzjVXG; incap_ses_297_1661922=ZmhYV5NcwBqzxmwnAigfBDomc2YAAAAACxwnlvZbb7CFaRp9tjshLQ==; NEXT_LOCALE=en; incap_ses_1693_1661922=8mXLcxf5vQlG8Xpdmr5+F9Emc2YAAAAAPvQBZy5lCnsMI+BZ18Ev8A==; incap_ses_1478_1661922=6SKZFvUlWXTddQD8PemCFE4nc2YAAAAAA1RDh3EUoMiBBdiGXfPQ1A==; incap_ses_1312_1661922=eCAYG5gKgzxp1GghHyk1Ek4nc2YAAAAAlnTH5BNlbAC1LJIWCODt7w==; visid_incap_1661977=16cGyvtzRra8vKfHr2A9ZFEnc2YAAAAAQUIPAAAAAADMAhX13R06Z8YwujKZNynu; incap_ses_1620_1661977=DqRIBU3C+34kbg1hfWV7FlInc2YAAAAAiPLDZ/2JDgOyj89/IJYPNg==; incap_ses_1298_1661922=Ncn1TpClNgcUq4UfMmwDElknc2YAAAAAmdTrIYsNQ6ZC6e/xvshofQ==; incap_ses_1242_1661922=6VduVlny/hIbFlBngHg8EVknc2YAAAAAmXy3veI/cbjc6tcTiVIIBw==; incap_ses_784_1661922=u2rxSlB1GH26U7Lr9lPhClonc2YAAAAAWOOPDabhIu0ZMt0+KTawQg==; incap_ses_1470_1661922=8lRtemcALVv+WF7USH1mFFonc2YAAAAAqvBHp4w2EcrZjekEuMgVkA==; incap_ses_1477_1661922=Mh9aFPrO8lqnVRdVv1t/FFsnc2YAAAAA3r+9W/o4q2yQuZxHq2zkCw==; incap_ses_1471_1661922=V7mLK/q1S05+yi95xwpqFFsnc2YAAAAATCOMzkDZ2t4TmDNbltnwgA==; incap_ses_1454_1661922=pLRFBNnCrGCYuuKHXqUtFFsnc2YAAAAAfokd3K1azj6T27Llmn+SHw==; incap_ses_1694_1661922=Shl0f8yXsHG5UAQBGUyCF1snc2YAAAAAVtuR9MnqX9Jn19fHywzIvw==; incap_ses_1695_1661922=XbMQcxSrs225ClmintmFF1snc2YAAAAAZ8OT0BxcyvzV774e4gD1gg==; incap_ses_1453_1661922=j7ErALXCV2NHx3Xh3xcqFH4nc2YAAAAAEwvSZrm3sNaQIcrWQMC+KQ==; incap_ses_8073_1661922=9brIcA+nwAt9QKGI0Q4JcH8nc2YAAAAArIMxv273dNb0zRpfVQP4Ew==; incap_ses_1474_1661922=iNyofeczyV2tBvRmQ7N0FH8nc2YAAAAAkOYmbRmihf6MV4n3L7Pe0g==; incap_ses_1254_1661922=NCgMA24cMEkZmdQhcBpnEYAnc2YAAAAAdCyQwrtHL6iTH6cgYCdSOw==; incap_ses_1479_1661922=F2gkW1Zq2VempJievHaGFIAnc2YAAAAAXORhxkhZy65Pob0+NSe0OA==; incap_ses_1239_1661922=CwXfKUsHYkWACCsmAtAxEcInc2YAAAAAo0sPqCFyneadtijLX6LWEA==; incap_ses_1697_1661922=wOWTRy7xlWZg4VXvlPSMF9Mnc2YAAAAAL20T7ZTFrR/9T2prq/xyGA==; incap_ses_1455_1661922=/EVUdmouh2r67vIq3TIxFNUnc2YAAAAAO8OoITT7cbmBNgSVShXUqg==; incap_ses_1696_1661922=RPZcdBBu7g5adORKFmeJF9Unc2YAAAAAL0xSyxp/4M7FFWvs1jYF/w==; incap_ses_1698_1661922=A6chIrX2Ux4QEwmUE4KQF9Ync2YAAAAAra6Nkzp2rclv4O1/QpoRIw==; nlbi_2349797=YxJ7CuodBlzbM3LdzMiLaQAAAABi0gLTFn/IU32wlaiS1BAH; visid_incap_2349797=OnuRGA2kQNmLG4tykzVdhxgoc2YAAAAAQUIPAAAAAADaz5t41q/CMNcbkvTPpVtd; incap_ses_1620_2349797=X9h1CFrxbgZ7Yg5hfWV7Fhkoc2YAAAAAZUl5DYNV49FzClBaH4qYIg==; incap_ses_1476_1661922=1Gt+QDhdcFDT3yeyQM57FBkoc2YAAAAAXyz5rYxAXxSeKjoQTjsiwA==; visid_incap_1662004=kXfuYW5QR9eU81kimD5Tawkpc2YAAAAAQUIPAAAAAACASSfC2yizOiftUuqoJiWT; incap_ses_1620_1662004=U7edJ34H83tjdg9hfWV7Fgopc2YAAAAA0swKSgO3W88iDHX3zwPBaw==; incap_ses_1240_1661922=yhSdLmuhp0TH2U4gg101EUEpc2YAAAAA7Uu/xHrExAwW91GiXDIjlg==; aceSession=1yUfZya9xdI2u1P1HyeMi4DY60z1qXfYqEOWBWcgEiqG0OCPP/1YRrw8kAk1Wvx8qxsxrNmpe4zxkZishPHU9aOsrlelX6+FfUhj/vSizzb5F5xuJifZlFzRIaSqFqNMNpljTLUzYjMsnEgzAf321Hoy6CaYEAujJrvXiL0f6RM5hyXrtf7cTOfVxOd6ShOq; incap_ses_787_1661922=bo81DiM15UOi9L/ca/zrCvwpc2YAAAAAMXhUMr+iYhP83rq/AFzO8w==; incap_ses_1241_1661922=TY6XYozjCnnu8KPCAes4Efwpc2YAAAAAfX07peUbcm6kbR+Xo13Rkg==; incap_ses_789_1661922=XjnpeqK1Wn9omf7WZhfzCioqc2YAAAAA5iLuZ/UyTMU7KdH0lIjfmw==; nlbi_2349797_2147483392=WDsEEVD4kDC0XgYBzMiLaQAAAADvOhOii0ERM6Ov6oQfHO+E; _ga_80QRY9FZ67=GS1.1.1718822940.1.1.1718823480.0.0.0; _ga_L6ZCHWX6DZ=GS1.1.1718822940.1.1.1718823480.0.0.0; _ga=GA1.1.1592596349.1718822122; _ga_Y0W8DGNBTB=GS1.1.1718822122.1.1.1718823606.0.0.0',
  'pragma': 'no-cache',
  'priority': 'u=0, i',
  'referer': 'https://www.metmuseum.org/policies/visitor-guidelines',
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
