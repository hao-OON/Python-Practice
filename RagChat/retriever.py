import json

def load_documents():
    with open("../QuotesCrawler/quotes_crawler_json.json",'r',encoding='utf-8') as f1:
        crawler = json.load(f1)
    with open("../QuotesCrawler/quotes_author_json.json",'r',encoding='utf-8') as f2:
        author = json.load(f2)

    documents = []
    for i in crawler:
        documents.append(i)
    for j in author:
        j['text'] = j['description']
        documents.append(j)

    return documents

def retrieve(query, documents):
    hits = []
    for i in documents:
        hit = {}
        if query in i['text']:
            occurrences = i['text'].count(query)
            hit['count'] = round(occurrences/len(i['text']),3)
            hit['text'] = i['text']
            hits.append(hit)
    sorted_hits = sorted(hits, key=lambda hit: hit['count'], reverse=True)
    return sorted_hits
if __name__ == '__main__':
    query = input()
    documents = load_documents()
    sorted_hits = retrieve(query, documents)
    for hit in sorted_hits[0:3]:
        # print(hit['count'],len(hit['text']),hit['text'][0:70])
        print(hit['text'][0:70])