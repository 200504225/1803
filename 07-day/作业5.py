money = int(input("请输入身价"))
height = int(input("请输入身高"))
nice = int(input("请输入颜值分"))
if money >= 100000 and height >= 180 and nice >= 80:
	print("高富帅")
elif money >= 1000000 and  nice >= 85:
	print("富帅")
elif nice >= 99:
	print("帅")
elif money < 100 and height < 160 and nice < 60:
	print("矮穷矬")
else:
	print("傻子")
