import random
a = random.randint(1,100)
b = 1
while b<=10:
	c = int(input("请输入数字:"))
	if c>a:
		print("猜大了")
	elif c<a:
		print("猜小了")
	else:
		print("猜对了")
		break
	b+=1
