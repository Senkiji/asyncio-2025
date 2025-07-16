import requests

respone = requests.get("https://httpbin.org/delay/3")
print(respone.status_code)