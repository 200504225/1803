
nu = int(input("请输入年份"))
if (nu%4 == 0 and nu%100 == 0 and nu%400 == 0):
	print("闰年")
else:
	print("平年")
