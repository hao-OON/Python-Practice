import json
from urllib.parse import urljoin
import requests
import bs4

def write(books):
    with open("book_crawler_json.json",'w',encoding='utf-8') as f:
        json.dump(books,f,ensure_ascii=False,indent=4)

def addbook(url):
    resp = requests.get(url,timeout=10)
    if resp.status_code != 200:
        exit(f"请稍后再试，状态码为：{resp.status_code}" )
    resp_content = resp.content.decode("utf-8")
    soup = bs4.BeautifulSoup(resp_content,"html.parser")
    pods =soup.find_all(class_ = 'product_pod')
    books = []
    for i in pods:
        book = {}
        book ['name'] = i.find('h3').find('a')['title']
        book ['price'] = float(i.find('p',class_ = 'price_color').get_text().replace('£',' '))
        book ['rating'] = i.find('p',class_ = 'star-rating')['class'][1]
        book ['stock'] = i.find('p',class_ = 'instock availability').get_text().strip()
        books.append(book)
    now_page =soup.find('li',class_ = 'next')
    if now_page:
        next_url = urljoin(url, now_page.find('a')['href'])
    else:
        next_url = None
    return books,next_url

def max_(all_books):
    ma = max(all_books,key=lambda x:x['price'])
    return ma

def min_(all_books):
    mi = min(all_books,key=lambda x:x['price'])
    return mi


def avg_(all_books):
    li = []
    for i in all_books:
        li.append(i['price'])
    avg_price = sum(li)/len(li)
    return round(avg_price,2)

all_books = []
url = "https://books.toscrape.com/"
while url:
    books,url = addbook(url)
    all_books.extend(books)
write(all_books)
print(len(all_books))
ma = max_(all_books)
mi = min_(all_books)
avg = avg_(all_books)
print(f"书库中最贵的书是{ma['name']},价格是{round(ma['price'],2)}")
print(f"书库中最便宜的书是{mi['name']},价格是{round(mi['price'],2)}")
print(f"书库中所有书的平均价格是{avg}")




