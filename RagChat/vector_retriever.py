import json
import requests
import os

def load_documents():
    with open("data/py_datastructures.json", "r", encoding="utf-8") as f:
        documents = json.load(f)
    return documents

def build_index(documents):
    new_count_ = []
    for i in documents:
        count_ = to_vector(i)
        new_count_.append(count_)
    return new_count_


def to_vector(input_):
    with open("embed_key.txt","r",encoding="UTF-8") as f:
        api_key = f.read()

    headers = {"Authorization":"Bearer " + api_key,
               "Content-Type":"application/json"}

    body =  {"model": "embedding-3",
             "input": input_}

    try:
        rep = requests.post("https://open.bigmodel.cn/api/paas/v4/embeddings",headers=headers,json = body,timeout=3)
    except requests.exceptions.ConnectionError:
        exit("请稍后再试")
    data = rep.json()
    return data['data'][0]['embedding']

def retrieve(query, documents):
    shuz = to_vector(query)
    index_ = {} ; data = {}
    data['time'] = os.path.getmtime("data/py_datastructures.json")
    data['size'] = os.path.getsize("data/py_datastructures.json")
    if os.path.exists("data/py_vecs.json"):
        with open( "data/py_vecs.json", "r", encoding="utf-8") as f:
            index_ = json.load(f)
        if index_['head'] != data:
            index_['head'] = data
            index_['body'] = build_index(documents)
            with open("data/py_vecs.json","w",encoding="utf-8") as f:
                json.dump(index_,f)
    else:
        index_['head'] = data
        index_['body'] = build_index(documents)
        with open("data/py_vecs.json","w",encoding="utf-8") as f:
            json.dump(index_,f)
    documentss = [] ; m = 0
    for i in index_['body']:
        document = {}
        document['text'] = documents[m]
        m += 1
        n = 0 ; sum_ = 0
        for j in i:
            sum_ += j * shuz[n]
            n += 1
        document['score'] = sum_
        documentss.append(document)
    sorted_documentss = sorted(documentss, key=lambda documentss: documentss['score'], reverse=True)
    return sorted_documentss

if __name__ == '__main__':
    docs   = load_documents()
    query = input("请输入你想查找的东西:")
    now_documents = retrieve(query, docs)
    print(len(now_documents))
    for i in now_documents:
        print(i)