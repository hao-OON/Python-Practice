import json
import requests
from bs4 import BeautifulSoup

url = 'https://docs.python.org/zh-cn/3/tutorial/datastructures.html'
response = requests.get(url, timeout=10)
soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
blocks = soup.find_all('dl')

texts = []
for block in blocks:
    texts.append(block.text.strip())
with open('data/py_datastructures.json', 'w',encoding='utf-8') as f:
    json.dump(texts, f,ensure_ascii=False,indent=2)
