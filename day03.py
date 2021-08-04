username = 'whq123'
password = '1121'
while True:
    user = input("请输入账号：")
    passwd = input('请输入密码：')
    if user == username and passwd == password:
        break
    else:
        print("账号密码不正确")
qi = 5000
kou = -500
jiang = 10000
import random
# 1.实现步骤
num = random.randint(0,10000)
count = 0
while True:
    count =  count + 1
    chose = input("输入您要的猜的数字：")
    chose = int(chose)
    if qi > 0:
        if chose > num:
            qi = qi + kou
            print("大了！","您现在有",qi,"金")
        elif chose < num:
            qi = qi + kou
            print("小了！","您现在有",qi,"金")
        else:
            num = random.randint(0,10000)
            qi = qi + jiang
            print("恭喜，您猜中了，本次数字为：",num,"，您本次输入了",count,"次！您现在有",qi,"金")
    else:
        print("GG")
        break