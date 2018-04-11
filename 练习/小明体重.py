i = float(input("请输入身高:\t"))
o = float(input("请输入体重:\t"))
p = (o/(i*i))
if p < 18.5:
	print("过轻")
elif ((p>= 18.5) and (p < 25)):
#elif p >= 18.5 and p < 25:
	print("正常")
elif ((p >= 25) and (p < 28)):
	print("过重")
elif ((p >=28 ) and (p < 32)):
	print("肥胖")
elif p > 32:
	print("严重肥胖")
else:
	print("输出错误")
