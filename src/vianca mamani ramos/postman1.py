import requests

url = "https://metmuseum.zendesk.com/embeddable/config"

payload = {}
headers = {
  'Cookie': '__cfruid=4d2dde06090df8e47e74ca0530f299a365c66ee6-1719203768'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
