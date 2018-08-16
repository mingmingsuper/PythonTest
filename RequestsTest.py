import requests

r = requests.get('https://www.liuandy.cn')
print(r.status_code)
# print(r.text)
print(r.headers)
