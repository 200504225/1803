a = 0
while a <= 0:
	i = int(input("请输入数字:\n"))
	o = int(input("请输入数字:\n"))
	sum = 0
	if i < o:
		for t in range(i,o):
			print(t)
			sum = sum+t
		a+=1
	else:
		print("输入错误")
	print(sum)
