import requests

with open("deepseek_key.txt","r",encoding="UTF-8") as f:
    api_key = f.read()

headers = {"Authorization":"Bearer " + api_key,
           "Content-Type":"application/json"}

messages = []
while True:
    user_input = input("(输入exit 退出)你:")

    if user_input == "exit":
        print("成功退出")
        break

    messages.append({"role": "user", "content": user_input})

    body = {"model": "deepseek-flash",
            "messages": messages}
    try:
        rep = requests.post("https://api.deepseek.com/chat/completions",headers=headers,json = body)
    except requests.exceptions.ConnectionError:
        exit("请稍后再试")


    if rep.status_code == 400:
        exit("你的箱子内容写错了，请检查")
    elif rep.status_code == 401:
        exit("你的api_key错误，请重新检查")
    elif rep.status_code == 402:
        exit("余额不足，请先充值再使用")
    elif rep.status_code == 422:
        exit("请修改你的参数")
    elif rep.status_code == 429:
        exit("请慢一点尝试")
    elif rep.status_code in (500, 503):
        exit("请等一下重试")
    if rep.status_code != 200:
        exit(f"请求失败，状态码：{rep.status_code}")

    data = rep.json()

    messages.append(data['choices'][0]['message'])

    print(data['choices'][0]['message']['content'])