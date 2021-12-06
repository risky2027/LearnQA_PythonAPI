import requests

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
response1 = requests.get(url)
print(response1.text)

response2 = requests.head(url, data={'method':'HEAD'})
print(response2.status_code)

response3 = requests.get(url, params={'method':'GET'})
print(response3.text)

dict = {"GET", "POST", "PUT", "DELETE"}
for item in dict:
    response = requests.get(url, params={'method':item})
    print("Requests.get", item, response.status_code, response.text)
    response = requests.post(url, data={'method':item})
    print("Requests.post", item, response.status_code, response.text)
    response = requests.put(url, data={'method':item})
    print("Requests.put", item, response.status_code, response.text)
    response = requests.delete(url, data={'method':item})
    print("Requests.delete", item, response.status_code, response.text)