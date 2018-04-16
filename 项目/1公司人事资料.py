zl =[]
def jm():
	print("*"*40)
	print("欢迎登录人事系统!".center(30," "))
	print("1:录入资料".center(28," "))
	print("2:修改资料".center(28," "))
	print("3:查找资料".center(28," "))
	print("4:删除资料".center(28," "))
	print("5:退出系统".center(28," "))

def xc():
	while True:
		xz = int(input("请输入选项"))
		if xz ==1:
			lr()
		elif xz == 2:
			xg()
		elif xz == 3:
			cz()
		elif xz == 4:
			sc()
		else:
			break
def lr():
	zd ={}
	number = int(input("请输入工号"))
	name = input("请输入名字")
	department = input("请输入部门")
	sex = input("请输入性别")
	weig = float(input("请输入身高米"))
	phone = int(input("请输入电话号码"))
	zd["number"] = number
	zd["name"] = name
	zd["department"] = department
	zd["sex"] = sex
	zd["weig"] = weig
	zd["phone"] = phone
	zl.append(zd)
	print(zl)


def xg():
	number = int(input("请输入工号"))
	flag = 0
	for ll in zl:
		if number == ll["number"]:
			flag = 1
			print("1:修改工号")
			print("2:修改名字")
			print("3:修改部门")
			print("4:修改性别")
			print("5:修改身高")
			print("6:修改电话")
			xx = int(input("请输入修改项"))
			if xx == 1:
				nn = int(input("请输入新工号"))
				ll["number"] = nn
				print("修改成功")
			elif xx == 2:
				nm = input("请输入新名字")
				ll["name"] =nm
				print("修改成功")
			elif xx == 3:
				nd = input("请输入新部门")
				ll["department"] = nd
				print("修改成功")
			elif xx == 4:
				ns = input("请输入性别")
				ll["sex"] =ns
				print("修改成功")
			elif xx == 5:
				nw = input("请输入新身高")
				ll["weig"] = nw
				print("修改成功")
			elif xx == 6:
				np = input("请输入新电话")
				ll["phone"] = np
				print("修改成功")
			else:
				print("输入错误")
				break
		else:
			print("工号错误")
							
def cz():
	number = int(input("请输入工号"))
	flag = 0
	for ll in zl:
		if number == ll["number"]:
			falg =1
			print("工号是:%d\n姓名是:%s\n部门是:%s\n性别是:%s\n身高是:%0.2f\n电话是:%d\n"%(ll["number"],ll["name"],ll["department"],ll["sex"],ll["weig"],ll["phone"]))
		else:
			print("工号错误")
def sc():
	number = int(input("请输入工号"))
	flag = 0
	for ll in zl:
		if number == ll["number"]:
			falg =1
			xz = int(input("确认删除--1  返回选项--2"))
			if xz == 1:
				zl.remove(ll)
				break
			else:
				continue
		else:

			print("工号错误")




jm()
xc()
