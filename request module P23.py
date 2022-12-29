# request module
import requests
payload = {"key1": "value1"}
# r = requests.get("https://www.w3schools.com/html/default.asp", params=payload)
r = requests.get("http://httpbin.org/get", params=payload)
# print(r)
# print(r.url)
print(r.json())

# post request
payload = {"user_name": "ram", "password": "123"}
res = requests.post("http://httpbin.org/post", data=payload)
# print(res.text)
# print(res.url)
print(res.json())

# other request methods
# r = requests.get("https://www.edureka.co/get")
# print(r.content)
# print(r.headers)
# print(r.status_code)
# print(r.cookies)
# result = r.json()
# print(result)
