import datetime
def mywrite():
    notes = input("请输入今天的记录：")
    mytime = datetime.datetime.now()
    s = mytime.strftime("%Y-%m-%d %H:%M:%S")
    with open("notes.json","a",encoding="utf-8") as f:
        f.write(s+" | "+notes+"\n")

def myread():
    with open("notes.json","r",encoding="utf-8") as f:
        test = f.readlines()
        for i in test:
            print(i)
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