import json
import requests
import os

def load_documents():
    with open("data/py_datastructures.json", "r", encoding="utf-8") as f:
        documents = json.load(f)
    return documents

def build_index(documents):
    vectors = []
    for text in documents:
        vector = to_vector(text)
        vectors.append(vector)
    return vectors


def to_vector(text):
    with open("embed_key.txt","r",encoding="UTF-8") as f:
        api_key = f.read()

    headers = {"Authorization":"Bearer " + api_key,
               "Content-Type":"application/json"}

    body =  {"model": "embedding-3",
             "input": text}

    try:
        response = requests.post("https://open.bigmodel.cn/api/paas/v4/embeddings",headers=headers,json = body,timeout=3)
    except requests.exceptions.ConnectionError:
        exit("请稍后再试")
    except requests.exceptions.Timeout :
        exit("请求超时")
    payload = response.json()
    return payload['data'][0]['embedding']

def retrieve(query, documents):
    query_vector = to_vector(query)
    index = {} ; stamp = {}
    stamp['time'] = os.path.getmtime("data/py_datastructures.json")
    stamp['size'] = os.path.getsize("data/py_datastructures.json")
    if os.path.exists("data/py_vecs.json"):
        with open( "data/py_vecs.json", "r", encoding="utf-8") as f:
            index = json.load(f)
        if index['head'] != stamp:
            index['head'] = stamp
            index['body'] = build_index(documents)
            with open("data/py_vecs.json","w",encoding="utf-8") as f:
                json.dump(index,f)
    else:
        index['head'] = stamp
        index['body'] = build_index(documents)
        with open("data/py_vecs.json","w",encoding="utf-8") as f:
            json.dump(index,f)
    hits = []
    for vector, text in zip(index['body'], documents):
        hit = {}
        hit['text'] = text
        score = 0
        for value, query_value in zip(vector, query_vector):
            score += value * query_value
        hit['score'] = score
        hits.append(hit)
    ranked = sorted(hits, key=lambda hit: hit['score'], reverse=True)
    return ranked

if __name__ == '__main__':
    documents = load_documents()
    query = input("请输入你想查找的东西:")
    hits = retrieve(query, documents)
    print(len(hits))
    for hit in hits:
        print(hit)
