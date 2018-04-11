print("*"*40)
print("欢迎来到名片系统!".center(30," "))
print("1:新增名片".center(30," "))
print("2:查找名片".center(30," "))
print("3:修改名片".center(30," "))
print("4:删除名片".center(30," "))
print("5:退出系统".center(30," "))
print("*"*40)

mp= []
while True:
	gn = int(input("请选择功能"))
	if gn == 1:
		flag = 0
		zd = {}
		na = input("请输入名字")
		for ll in mp:
			if na == ll["na"]:
				flag =1
				break
		if flag == 1:
			print("名字重复，请重新输入")
			continue
		zw = input("请输入职务")
		dh = input("请输入电话")
		gs = input("请输入公司")
		dz = input("请输入地址")
		zd["na"] = na
		zd["zw"] = zw
		zd["dh"] = dh
		zd["gs"] = gs
		zd["dz"] = dz
		mp.append(zd)
		print("新增成功")
	elif gn == 2:
		na = input("请输入名字")
		flag = 0
		for ll in mp:
			if na == ll["na"]:
				flag = 1
				print("名字是:%s\n职务是:%s\n电话是:%s\n公司是:%s\n地址是:%s\t"%(ll["na"],ll["zw"],ll["dh"],ll["gs"],ll["dz"]))
				break
		if flag == 0:
			print("输入错误")
			continue
	elif gn == 3:
		na = input("请输入名字")
		for ll in mp:
			if na == ll["na"]:
				print("1:修改名字".center(20," "))				
				print("2:修改职务".center(20," "))				
				print("3:修改电话".center(20," "))
				print("4:修改公司".center(20," "))
				print("5:修改地址".center(20," "))
				xg = int(input("请输入修改选项"))
				if xg ==1:
					na = input("请输入新名字")
					ll["na"] = na
					print("修改成功")
				elif xg == 2:
					zw = input("请输入新职务")
					ll["zw"] = zw
					print("修改成功")
				elif xg == 3:
					dh = input("请输入新电话")
					ll["dh"] = dh
					print("修改成功")
				elif xg == 4:
					gs = input("请输入新公司")
					ll["gs"] = gs
					print("修改成功")
				elif xg == 5:
					dz = input("请输入新地址")
					ll["dz"] =dz
					print("修改成功")
				else:
					print("输入错误")
	elif gn == 4:
		na = input("请输入名字")
		flag = 0
		for ll in mp:
			if na == ll["na"]:
				flag =1
				qd = int(input("确认删除--0  取消删除--1"))
				if qd == 0:
					mp.remove(ll)
					print("删除成功")
		if flag ==0:
			print("删除失败")
	else:
		break
