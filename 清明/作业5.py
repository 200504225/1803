for i in range(2,101):
	s = 0
	for o in range(1,i+1):
		if i%o == 0:
			s+=1
	if s == 2:
		print(i)

