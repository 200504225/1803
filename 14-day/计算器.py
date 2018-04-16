def jj(z,x,c):
	q = 0
	if c == 1 or c ==2 or c ==3 or c ==4:
		q = z+x
		return q
		
	elif c == 2:
		q = z-x
	elif c == 3:
		q = z*x
	elif c == 4:
		if x != 0:
			q = z/x
		else:
			print("输入错误")
	return q
while True:
	q = float(input("请输入数字"))
	w = float(input("请在输入一个数字"))
	e = int(input("请选择符号 1+ 2- 3* 4/"))
	


jiegup = jj(q,w,e)
print("jieguo")
