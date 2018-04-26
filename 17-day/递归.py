def i_num(num):
	if num ==1:
		return 1

	else:
		return num*i_num(num-1)



i_num(5)
