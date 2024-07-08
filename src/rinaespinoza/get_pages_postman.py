import requests

url = "http://localhost/wordpress/wordpress/wp-json/wp/v2/posts?mo_rest_api_test_config=jwt_auth"

payload = {}
headers = {
  'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjEsIm5hbWUiOiJhdXRvIiwiaWF0IjoxNzE4ODMwOTM1LCJleHAiOjE4NzY1MTA5MzV9.zTHQ32OUjb4zeNVFPgloZ3Rlgxe1QSKyGS0YKBaefFM'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
