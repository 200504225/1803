def ii(q,w,e):    
	if e == 1:
		return q+w
	elif e == 2:
		return q-w
	elif e == 3:
		return q*w
	elif e == 4:
		if x != 0:
			return q/w
	else:
		print("输入错误")
while True:
	q = float(input("请输入数字"))
	w = float(input("请在输入一个数字"))
	e = int(input("请选择符号 1+ 2- 3* 4/"))
	jieguo = ii(q,w,e)
	print(jieguo)

