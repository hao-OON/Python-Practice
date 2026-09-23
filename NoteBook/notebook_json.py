import datetime
import json
def myread():
    with open("notes.json","r",encoding="utf-8") as data:
        records = json.load(data)
        for i in records:
            print(i['time'])
            print(i['content'])

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

while True:
    n = input("(1 记，2 看，0 退出)\n请选择你需要的操作：")
    if n == '1':
        mywrite()
    elif n == '2':
        myread()
    elif n == '0':
        break
    else:
        print("您输入的内容不符合要求，请重新输入：")