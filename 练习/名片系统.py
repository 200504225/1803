print("*"*40)
print("欢迎来到名片系统!".center(30,"-"))
print("1:新增名片".center(36," "))
print("2:查找名片".center(36," "))
print("3:修改名片".center(36," "))
print("4:删除名片".center(36," "))
print("5:退出系统".center(36," "))
print("*"*40)
mp = []
while True:
	gn = int(input("请选择功能"))
	if gn == 1:
		zd = {}
		flag =0
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
		zd["dz"] =dz
		mp.append(zd)
		print("添加成功")
	elif gn == 2:
		na = input("请输入名字")
		flag =0
		for ll in mp:
			if na == ll["na"]:
				flag =1
				print(zd["na"],zd["zw"],zd["dh"],zd["dz"])
		if flag == 0:
			print("查无此人")
	elif gn == 3:
		print("修改")

	elif gn == 4:
		na = input("请输入名字")
		flag =0
		for ll in mp:
			if na == ll["na"]:
				flag =1
				xz = int(input("0--确认删除 1--取消删除"))
				if xz == 0:
					mp.remove(ll)
					print("删除成功")
					break
		if flag ==0:
			print("删除失败")
	else:
		break
			
		
