x = float(input("请输入数字"))
y = float(input("请输入数字"))
fuhao = input("请输入+-*/")
if fuhao == "+":
	print(x+y)
elif fuhao == "-":
	print(x-y)
elif fuhao == "*":
	print(x*y)
elif fuhao == "/":
	print(x/y)
else:
	print("输入错误")
