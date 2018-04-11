i = float(input("请输入身高:"))
s = float(input("请输入颜值:"))
d = float(input("请输入身价:"))
if i >= 180 and s >= 80 and d >= 100000:
	print("高富帅")
elif s >= 80 and d >= 100000:
	print("富帅")
elif s >= 90:
	print("帅哥")
else:
	print("屌丝")
