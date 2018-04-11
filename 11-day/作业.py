i = []
o = []
p = 3
while p > 0:
	j = {}
	na = input("请输入名字")
	if na in o:
		print("姓名重复，请重新输入")
		continue;
	o.append(na)
	ag = input("请输入年龄")
	se = input("请输入性别")
	qq = input("请输入QQ号")
	wi = input("请输入体重")
	j["na"]=na
	j["ag"]=ag
	j["se"]=se
	j["qq"]=qq
	j["wi"]=wi
	i.append(j)
	p = p-1;
for l in i:
	print(l)



