import requests

url = "https://collectionapi.metmuseum.org/public/collection/v1/search?q=Medieval+Art"

payload = {}
headers = {
  'Cookie': 'incap_ses_545_1662004=FcA/f40BVExiNT8atDqQB9dGc2YAAAAAl7g8Q5OX2guK2f9dc6lKwA==; visid_incap_1662004=M2opLTipR0KHFoTvKohXYh7OcGYAAAAAQUIPAAAAAAC+ShrzCsjRRySGgAgX28Ib'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
