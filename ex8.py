import json
import time
import requests

url = "https://playground.learnqa.ru/ajax/api/longtime_job"
response = requests.get(url)
json_text = json.loads(response.text)
token = {'token':json_text['token']}

response = requests.get(url, params=token)
print(response.text)

time.sleep(10)

response = requests.get(url, params=token)
print(response.text)
