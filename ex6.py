import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
print(response.history)
for resp in response.history:
    print(resp.status_code, resp.url)
print(response.url)