import json
from urllib.parse import urljoin

import bs4
import requests

def quotes_crawler(url):
    requ = requests.get(url, timeout=10)
    if requ.status_code != 200:
        exit(f"请稍后再试，状态码为：{requ.status_code}")
    soup = bs4.BeautifulSoup(requ.content.decode('utf-8'), 'html.parser')
    pods = soup.find_all(class_='quote')
    quotes_json = []
    for i in pods:
        quotes = {}
        quotes['author_url'] = urljoin (url, i.find('a')['href'])
        quotes['text'] = i.find('span', class_ = 'text').get_text()
        quotes['author'] = i.find('small' , class_ = 'author').get_text()

        tag = i.find_all('a',class_='tag')
        tags = []
        for j in tag:
            tags.append(j.get_text())
        quotes['tags'] = tags
        quotes_json.append(quotes)
    next_page = soup.find('li' , class_='next')
    if next_page:
        next_url = urljoin (url, next_page.find('a')['href'])
    else:
        next_url = None
    return quotes_json, next_url

def write_quotes():
    url = "https://quotes.toscrape.com"
    quotes_json = []
    i = 0
    while url:
        i += 1
        print(i, url)
        quotes, url = quotes_crawler(url)
        quotes_json.extend(quotes)
    return quotes_json

quotes_json = write_quotes()

quotes = []
count = 0
for i in quotes_json:
    judge = True
    for j in quotes:
        if i['author_url'] == j['author_url']:
            judge = False
    if judge == False:
        continue
    url = i['author_url']
    count += 1
    print(count,url)
    requ = requests.get(url, timeout=10)
    if requ.status_code != 200:
        exit(f"请稍后再试，状态码为：{requ.status_code}")
    soup = bs4.BeautifulSoup(requ.content.decode('utf-8'), 'html.parser')

    author_data = {}
    author_data['author_url'] = url
    author_data['name'] = soup.find('h3',class_ = 'author-title').get_text()
    author_data['birthday'] = soup.find('span',class_ = 'author-born-date').get_text()
    author_data['location'] = soup.find('span', class_='author-born-location').get_text().strip()
    author_data['description'] = soup.find('div', class_='author-description').get_text().strip()
    quotes.append(author_data)

with open('quotes_crawler_json.json', 'w',encoding='utf-8') as f:
    json.dump(quotes_json, f, ensure_ascii=False, indent=4)
with open("quotes_author_json.json",'w',encoding='utf-8') as f:
    json.dump(quotes,f,ensure_ascii=False,indent=4)
