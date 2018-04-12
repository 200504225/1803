print("*"*40)
print("学生管理系统".center(30," "))
print("1:录入成绩".center(30," "))
print("2:修改成绩".center(30," "))
print("3:查询成绩".center(30," "))
print("4:删除成绩".center(30," "))
print("5:打印菜单".center(30," "))
print("6:打印全部成绩".center(28," "))
print("7:退出系统".center(30," "))
print("*"*40)
cj = []
while True:
	gn = int(input("请选择功能"))
	if gn == 1:
		zd = {}
		flag = 0
		xh = int(input("请输入学号"))
		for ll in cj:
			if xh == ll["xh"]:
				flag = 1
				break
		if flag == 1:
			print("学号重复，请重新输入")
			continue
		xm = input("请输入姓名")
		zd["学号"] = xh
		zd["姓名"] = xm
		o = 1
		while o <3:	
			k = input("请输入科目")
			v = float(input("请输入成绩"))
			o+=1
			zd[k] = v
		cj.append(zd)

		print(cj)

	elif gn == 2:#修改
		xh = int(input("请输入学号"))
		flag =0
		for ll in cj:
			if xh == ll["学号"]:
				flag =1
				km = input("请输入科目")
				for oo in cj:
					if km == oo[k]:
						qq = float(input("请输入成绩"))
						zd[k]= qq
						print("修改成功")
		if flag == 0:
			print("无此学号")
			continue
	elif gn == 3:
		xh = int(input("请输入学号"))
		flag =0
		for ll in cj:
			if xh == ll["学号"]:
				flag =1
				print(cj)
		pass
	elif gn == 4:
		flag = 0
		xh = int(input("请输入学号"))
		for ll in cj:
			if cj == ll["xh"]:
				flag =1
		pass
	elif gn == 5:
		xh = int(input("请输入学号"))
		pass
	elif gn == 6:
		xh = int(input("请输入学号"))
		pass
	elif gn == 7:
		ex = int(input("确认--1  取消--2"))
		if ex == 1:
			break
		else:
			continue
		
