import requests

url = "https://cdn.sanity.io/images/cctd4ker/production/2b5c84a170e8e9a4cd3eac74c25cc548b7cb147c-1080x1080.jpg?w=1080&q=75&fit=clip&auto=format"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)