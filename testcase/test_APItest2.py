import requests

r=requests.get("https://www.google.com.tw/")
print(r.status_code)
print(r.cookies)