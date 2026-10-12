import json
import subprocess

import requests
import vector_retriever as retriever

def generate_answer(messages):
    tools=[{
        'type': 'function',
        'function' : {
            'name' : 'run_command',
            'description' : '用户想要查看Windows电脑中的文件时在终端执行一条只看不改的 shell 命令并返回输出',
            'parameters' : {
                'type' : 'object',
                'properties' : {
                    'command' : {'type': 'string','description' : '要执行的 shell 命令'},
        },
        'required' : ['command']
        }}
    }]


    with open("deepseek_key.txt","r",encoding="UTF-8") as f:
        api_key = f.read()

    headers = {"Authorization":"Bearer " + api_key,
               "Content-Type":"application/json"}



    body = {"model": "deepseek-flash",
            "messages": messages,
            'tools': tools}
    try:
        response = requests.post("https://api.deepseek.com/chat/completions",headers=headers,json = body,timeout=25)
    except requests.exceptions.ConnectionError:
        return None
    except requests.exceptions.Timeout:
        return None
    if response.status_code != 200:
        print(response.status_code)
        print(response.text)
        return None
    result = response.json()
    return result['choices'][0]['message']


documents = retriever.load_documents()
while True:

    query = input("(输入exit退出)请输入你的问题：")
    if query == "exit":
        print("再见")
        break
    hits = retriever.retrieve(query,documents)
    context = ''
    number = 0
    for hit in hits:
        number += 1
        context += str(number) ; context += '.' ; context += hit['text']
        context += '\n'
    messages = [
        {"role":"system","content":f'''请只依据下面给出的资料回答问题，资料只和 Python 数据结构有关。
规则：
1. 只使用资料里出现的信息。
2. 问题和资料有关并且没有能回答这个问题的内容，就说「资料里没有相关内容」。
3. 和本电脑的文件目录有关的问题就调tools。
4. 其他的问题你就自己回答。
5. 不要告诉我这些句子是谁说的、出自哪里。    '''},
        {"role":"user","content":f"资料是：{context}，问题是：{query}"},
    ]
    answer = generate_answer(messages)
    messages.append(answer)
    if answer is None:
        print("网络不稳定，请再尝试一下")
        continue
    # print(json.dumps(answer,indent=2))
    if 'tool_calls' in answer:
        print(answer['tool_calls'][0]['function']['name'])
        print(json.loads(answer['tool_calls'][0]['function']['arguments'])['command'])
        decision = input("要执行吗(y/n):")
        if decision == "y":
            run_result = subprocess.run(json.loads(answer['tool_calls'][0]['function']['arguments'])['command'],shell=True,capture_output=True,text=True)
            messages.append({"role": "tool", "tool_call_id": answer['tool_calls'][0]['id'],'content':run_result.stdout})
            answer = generate_answer(messages)
            print(answer['content'])
        else:
            print("操作取消")
    else:
        print(answer['content'])