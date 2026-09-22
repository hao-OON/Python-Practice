import datetime

mytime = datetime.datetime(2027, 3, 1) - datetime.datetime.now()
x = mytime.seconds
# print(mytime)
# print("天  ",time.days)  #天
# print(time.seconds)
# print("时  ",time.seconds // 3600)  #时
# print("分  ",(time.seconds % 3600 - time.seconds % 60)//60)
# print("秒  ",time.seconds % 60)  #秒
print(f"距离2027年3月1日还有{mytime.days}天{x // 3600}时{x % 3600 // 60}分{x % 60}秒")