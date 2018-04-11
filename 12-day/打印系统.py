print("*"*40)
print("欢迎来到名片系统!".center(30,"-"))
print("1:新增名片".center(30," "))
print("2:查找名片".center(30," "))
print("3:修改名片".center(30," "))
print("4:删除名片".center(30," "))
print("5:退出系统".center(30," "))
print("*"*40)
mp = []
while True:
	gn = int(input("请选择功能"))
	if gn == 1:
		print("新增\n")
		flag = 0
		zd = {}
		na = input("请输入名字")
		for ll in mp:
			if na == ll["na"]:
				flag = 1
				break
		if flag == 1:
			print("名字重复，请重新输入")
			continue
		zw = input("请输入职务")
		dh = input("请输入电话")
		dz = input("请输入地址")
		zd["na"] = na
		zd["zw"] = zw
		zd["dh"] = dh
		zd["dz"] = dz
		mp.append(zd)
	elif gn == 2:
		na = input("请输入名字")
		flaa = 0
		for ii in mp:
			if na  == ii["na"]:
				flaa = 1
				print("名字是:%s\n职务是:%s\n电话是:%s\n地址是:%s"%(ii["na"],ii["zw"],ii["dh"],ii["dz"]))
				break
		if flaa == 0:
			print("查无此人")
			continue
	elif gn == 3:
		na = input("请输入名字")
		for ll in mp:
			if na == ll["na"]:
				print("1:修改名字".center(30," "))
				print("2:修改职务".center(30," "))
				print("3:修改电话".center(30," "))
				print("4:修改地址".center(30," "))
				xn = int(input("请选择修改项"))
				if xn == 1:
					na = input("请输入新名字")
					ll["na"] = na
					print("修改成功")
				elif xn == 2:
					zw = input("请输入新职务")
					ll["zw"] = zw
					print("修改成功")
				elif xn == 3:
					dh = int(input("请输入新电话"))
					ll["dh"] =dh
					print("修改成功")
				elif xn == 4:
					dz = input("请输入新地址")
					ll["dz"] =dz
					print("修改成功")
				else:
					print("输入错误")
	elif gn == 4:
		flgg =0
		na = input("请输入名字")
		for jj in mp:
			if na == jj["na"]:
				flgg =1
				qr = int(input("确认请按-- 0  返回请安-- 1"))
				if qr == 0:
					mp.remove(jj)
					print("删除成功")
					break
		if flgg == 0:
			print("删除失败")
	else:
		break
