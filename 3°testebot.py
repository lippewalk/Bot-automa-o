import requests 

proxy = '35.185.196.38:3128'

r = requests.get('https://httpbin.org/ip', proxies={'htpp': proxy, 'https': proxy}, timeout=3)
print(r.json())

