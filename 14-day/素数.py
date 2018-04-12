def i(q,w):
	for i in range(q,w):
		flag = 0
		for j in range(q,i):
			if i % j == 0:
				flag =1
				break
		if flag == 0:
			print(i)

while True:
	q = int(input("请在输入数字"))
	w = int(input("请在输入数字"))
	i(q,w)
