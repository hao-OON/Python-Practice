import datetime
import json

def myread():
    with open("notes.json","r",encoding="utf-8") as data:
        records = json.load(data)
        for i in records:
            print(i['time'])
            print(i['content'])
            print("-----------------------------")

def mywrite():
    mytime = datetime.datetime.now()
    s = mytime.strftime("%Y-%m-%d %H:%M:%S")
    note = {}
    note['time'] = s
    note['content'] = input("请输入您要记录的内容：")

    with open("notes.json","r",encoding="utf-8") as data:
        records = json.load(data)
        records.append(note)

    with open("notes.json","w",encoding="utf-8") as data1:
        json.dump(records,data1,ensure_ascii=False,indent=2)

def mysearch():
    with open("notes.json","r",encoding="utf-8") as f:
        records = json.load(f)

    timesearch = input("请输入你想查询的时间：")
    keys = input("请输入你想查询的关键词：")
    if timesearch == '' and keys == '':
        print("你没有填写查询条件，请重新操作")
        return
    judge = False
    for i in records:
        if (timesearch != "" and timesearch in i['time']) or (keys != "" and keys in i['content']):
            print(i['time'])
            print(i['content'])
            print("-----------------------------")
            judge = True

    if not judge:
        print("没有搜索到你查找的内容")

while True:
    n = input("(1 记，2 看，3 搜，0 退出)\n请选择你需要的操作：")
    if n == '1':
        mywrite()
    elif n == '2':
        myread()
    elif n == '3':
        mysearch()
    elif n == '0':
        break
    else:
        print("您输入的内容不符合要求，请重新输入：")
