import requests

url = "https://store.metmuseum.org/customer/section/load/?sections=cart&force_new_section_timestamp=false&_=1719201277370"

payload = {}
headers = {
  'Cookie': 'PHPSESSID=ac62b0942f07755d8a0b3ac3fc0b26c9'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)