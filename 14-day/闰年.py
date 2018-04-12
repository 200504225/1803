def i(w):
	if w%400 == 0 and w%4 ==0: 
		print("%d是闰年"%w)
	elif w%100 != 0:
		print("%d是闰年"%w)
	else:
		print("%d平年"%w)


w = int(input("请输入年份"))
i(w)
