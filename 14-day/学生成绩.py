print("*"*40)
print("学生管理系统".center(30," "))
print("1:录入成绩".center(30," "))
print("2:修改成绩".center(30," "))
print("3:查询成绩".center(30," "))
print("4:删除成绩".center(30," "))
print("5:打印全部成绩".center(28," "))
print("6:退出系统".center(30," "))
print("*"*40)
cj = []
while True:
	gn = int(input("请选择功能"))
	if gn == 1:
		zd = {}
		flag = 0
		xh = int(input("请输入学号"))
		for ll in cj:
			if xh == ll["学号"]:
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
		print("录入成功")
		print(cj)

	elif gn == 2:#修改
		xh = int(input("请输入学号"))
		flag =0
		for ll in cj:
			if xh == ll["学号"]:
				flag =1
				km = input("请输入科目")
				for k,v in zd.items():
					if k == km:
						qq = float(input("请输入成绩"))
						zd[k]= qq
						print("修改成功")
						break
		if flag == 0:
			print("无此学号")
			continue
	elif gn == 3:
		xz = int(input("查看全部--1  查看个人--2"))
		if xz == 1:
			print(cj)
		elif xz == 2:
			xh = int(input("请输入学号"))
			flag =0
			for ll in cj:
				if xh == ll["学号"]:
					flag =1
					print(ll)
			else:
				("学号错误")
		else:
			print("输入错误")
	elif gn == 4:#删除
		flag = 0
		xh = int(input("请输入学号"))
		for ll in cj:
			if xh == ll["学号"]:
				flag =1
				cj.remove(ll)
				print("删除成功")
		else:
			print("删除失败")

	elif gn == 5:#打印全部成绩
		print(cj)
	elif gn == 6:#退出
		ex = int(input("确认--1  取消--2"))
		if ex == 1:
			break
	else:
		continue
		
