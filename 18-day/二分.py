list = [ 1,3,5,7,9,11,12,13,30,46,]
key = 11
nub = int(len(list)/2)
if key in list:
	while True:
		if list[nub] > key:
			nub = nub -1
		elif list[nub] < key:
			nub = nub +1
		elif list[nub] == key:
			print("数字%d在索引%d的位置"%(key,nub))
			break
