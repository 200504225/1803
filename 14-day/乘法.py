def i():
	while True:
		z = int(input("请在输入数字"))
		x = int(input("请在输入数字"))
		for q in range(z,x):
			for w in range(1,q+1):
				print("%d*%d=%d\t"%(w,q,q*w),end = "")
			print("")

i()
