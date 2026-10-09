import requests
import vector_retriever as retriever

def generate_answer(context,query):
    with open("deepseek_key.txt","r",encoding="UTF-8") as f:
        api_key = f.read()

    headers = {"Authorization":"Bearer " + api_key,
               "Content-Type":"application/json"}

    messages = [
        {"role":"system","content":'''请只依据下面给出的资料回答问题。
    
    规则：
    1. 只使用资料里出现的信息。
    2. 如果资料里没有能回答这个问题的内容，就直接回答"资料里没有相关内容"，
       不要补充任何别的内容。
    3. 不要告诉我这些句子是谁说的、出自哪里。'''},
        {"role":"user","content":f"资料是：{context}，问题是：{query}"},
    ]

    body = {"model": "deepseek-flash",
            "messages": messages}
    try:
        rep = requests.post("https://api.deepseek.com/chat/completions",headers=headers,json = body,timeout=5)
    except requests.exceptions.ConnectionError:
        return None

    data = rep.json()
    return data['choices'][0]['message']['content']

documents = retriever.load_documents()
while True:
    query = input("(输入exit退出)请输入你的问题：")
    if query == "exit":
        print("再见")
        break
    sorted_hits = retriever.retrieve(query,documents)
    context = ''
    i = 0
    for hit in sorted_hits[0:3]:
        i += 1
        context += str(i) ; context += '.' ; context += hit['text']
        context += '\n'
    data = generate_answer(context,query)
    if data is None:
        print("网络不稳定，请再尝试一下")
        continue
    print(data)