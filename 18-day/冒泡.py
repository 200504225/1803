list = [13,6,10,21,30,50,4,89,2]
for i in range(len(list)):
	for j in range(i+1,len(list)):
		if list[i] > list[j]:
			list[i],list[j] = list[j],list[i]


print(list)
key = 4
nub = int(len(list)/2)
if key in list:
	while True:
		if list[nub] > key:
			nub = nub -1
		elif list[nub] < key:
			nub = nub +1
		elif list[nub] == key:
			print("数字%d在索引%d"%(key,nub))
			break
