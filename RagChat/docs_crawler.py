import json
import requests
from bs4 import BeautifulSoup

url = 'https://docs.python.org/zh-cn/3/tutorial/datastructures.html'
response = requests.get(url, timeout=10)
response.raise_for_status()
soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
blocks = soup.find_all('dl')

texts = []
for block in blocks:
    texts.append(block.text.strip())

if len(texts) == 0:
    exit("一块资料都没抓到 —— 文件保持原样不写，避免把已有资料清空")

with open('data/py_datastructures.json', 'w',encoding='utf-8') as f:
    json.dump(texts, f,ensure_ascii=False,indent=2)
print("已写入", len(texts), "块资料")
