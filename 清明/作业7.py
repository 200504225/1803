zm = 0
for i in range(1,13):
	if i ==1 or i ==3 or i ==5 or i ==7 or i == 8 or i ==10 or i ==12:
		d = 31
	elif i == 2:
		d = 28
	else:
		d = 30
	if i == 1 or i == 12:
		l = 32
	elif i == 2 or i == 11:
		l = 18
	elif i == 3 or i == 10:
		l = 7
	elif i == 4 or i == 9:
		l = 80
	elif i == 5 or i == 8:
		l = 34
	else:
		l = 70
	k = 0
	for s in range(1,2*d+1):
		if l <= 6:
			m = 3
		elif l > 6 and l <= 12:
			m = 4
		elif l > 12 and l <= 22:
			m = 5
		elif l > 22 and l <= 32:
			m = 6
		elif l > 32:
			if(l-32)%20 == 0:
				m = 6+(l-32)/20
			else:
				m = 6+int((l-32)/20)+1
		if k > 100 and k <= 150:
			k+=float(0.8*m)
		elif k > 150 and k <= 150:
			k+=loat(0.5*m)
		else:
			k+=m
	print("%d月花%0.2f元"%(i,k))
	zm+=k
print("一年花%0.2f元"%zm）
