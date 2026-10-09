import json

import requests
from bs4 import BeautifulSoup

url = 'https://docs.python.org/zh-cn/3/tutorial/datastructures.html'
requ = requests.get(url, timeout=10)
beau = BeautifulSoup(requ.content.decode('utf-8'), 'html.parser')
pods = beau.find_all('section')
pod1 = beau.find_all('dl')

quotes_json = []
for j in pod1:
    quotes_json.append(j.text.strip())
with open('data/py_datastructures.json', 'w',encoding='utf-8') as f:
    json.dump(quotes_json, f,ensure_ascii=False,indent=2)


