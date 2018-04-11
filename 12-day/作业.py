'''
l = []
k = []
q = 0
while True:
	if q == 3:
		break
	w = {}
	na = input("请输入名字")
	age = int(input("请输入年龄"))
	sex = input("请输入性别")
	qq = input("请输入QQ")
	we = float(input("请输入体重"))

	if na not in k:
		w["na"] = na
		w["age"] = age
		w["sex"] = sex
		w["qq"] = qq
		w["we"] = we
		l.append(w)
		k.append(na)
		print(l)
		q+=1
	else:
		print("名字重复")
age_sum =0
for i in l:
	 age_sum = age_sum+i.get("age")
	 print(i)
print("年龄的平均值是%0.2f"%(age_sum/len(l)))
'''

l = []
p = []
o = 0
while True:
	if o == 3:
		break
	w = {}
	na = input("请输入名字")
	sex = input("请输入性别")
	age = int(input("请输入年龄"）
	qq = input("请输入QQ")
	wg = input("请输入重量")
	for na in p:
		w["na"]=na
		w["sex"]=sex
		w["age"]=age
		w["qq"]=qq
		w["wg"]=wg
		l.append(w)
		p.append(na)
		print(l)
		o+=1
	else:
		print("名字重复")

sun=0
for i in l:
