i = float(input("请输入数字"))
o = float(input("请输入数字"))
p = input("请输入符号 +-*/")
if p == "+":
	print("%d"%(i+o))
elif p == "-":
	print("%d"%(i-o))
elif p == "*":
	print("%d"%(i*o))
elif p == "/":
	print("%d"%(i/o))
else:
	print("输入错误")

