import requests

url = "	https://webhook.site/5f8460db-f280-41ca-9311-001ed9435ebc"

payload = {"plato":"pasta", "cantidad":2}
query_params = {"nombre":"Paco"}
response = requests.post(url, data=payload, params=query_params)
# print(response.status_code)
# print(response.text)