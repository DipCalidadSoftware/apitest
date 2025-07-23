import requests

url = "https://collectionapi.metmuseum.org/public/collection/v1/objects"

payload = {}
headers = {
  'Cookie': 'incap_ses_624_1662004=0gXhbFKKrBFFI6vZ8uSoCBMjgGgAAAAADy9UIQYBnO3Fy5uVYiXaew==; visid_incap_1662004=XZNwz29fTym9B8xac0FsF3nCfmgAAAAAQUIPAAAAAACPt25sEfXvh5rK+r4L0qXx'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
