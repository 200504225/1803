import random
dn = random.randint(1,100)
for i in range(100):
	wj = int(input("请输入数字"))
	if wj > dn:
		print("猜大了")
	elif wj < dn:
		print("猜小了")
	else:
		print("猜对了")
		break	
