import time
from random import randint
list = []
def rz():
	zl= {}
	name = input("请输入名字:")
	pos = input("请输入职务:")
	sa = float(input("请输入薪水:"))
	create_time = randint(0,1524190943)
	zl["name"] = name
	zl["pos"] = pos
	zl["sa"] = sa
	zl["create_time"]  = create_time
	list.append(zl)
	print("录入成功")

def cz():
	name = input("请输入名字")
	for temp in list:
		if name == temp["name"]:
			print("名字是:%s"%name)
			now = int(time.time())
			diff = now - temp["create_time"]
			day = diff / 86400
			print("薪水%f"%(temp["sa"]/30*day))
			break
def lx():
	name = input("请输入名字")
	for temp in list:
		if name == temp["name"]:
			print("名字是:%s"%name)
			now = int(time.time())
			diff = now - temp["create_time"]
			day = diff / 86400
			print("薪水%f"%(temp["sa"]/30*day))
			list.remove(temp)
			print("离职结算")

def dl():
	print("员工系统".center(20,"*"))
	print("1.员工入职")
	print("2.查找员工")
	print("3.员工离职")
	print("4.退出系统")
	while True:
		xz = int(input("请选择功能"))
		if xz == 1:
			rz()
		elif xz == 2:
			cz()
		elif xz == 3:
			lx()
		else:
			break


dl()
