#1---石头
#2---剪刀
#3---不
import random
comput = random.randint(1,3)

user = int(input("请输入1---石头 剪刀---2 布---3")
if (user==1 and comput==2) and (user==2 or comper==3) and (user==3 or comper==1):
	print("玩家赢")
elif user == comput:
	print("平局")
else:
	print("电脑赢")
