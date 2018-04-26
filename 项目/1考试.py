list=[]
def grade():
	for w in range(5):
		zd={}
		na = input("请输入名字")
		la = float(input("请输入语文成绩"))
		ma = float(input("请输入数学成绩"))
		en = float(input("请输入英语成绩"))
		zd["na"] = na
		zd["la"] = la
		zd["ma"] = ma
		zd["en"] = en
		sun = (ma+la+en)
		zd["sun"] = sun
		ave = sun/3
		zd["ave"] = ave
		list.append(zd)
		print("名字是%s\t语文成绩:%0.1f\t数学成绩:%0.1f\t英语成绩:%0.1f\t平均成绩:%0.1f\t总分:%0.1f"%(na,la,ma,en,ave,sun))




grade()
