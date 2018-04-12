#def renkou():
'''
list = [{"beijing":{"mianji":1290,"remkou":123123},"shanghai":{"mianji":12331,"renkou":123123}}]
for i in list:
	print(i)
	for o in i.keys():
		print(o)
		for k in i[o].keys():
			print(o,k,i[o][k])
	'''
list = [{"beijing":{"mianji":1290,"remkou":123123},"shanghai":{"mianji":12331,"renkou":123123}}]
def jj():
	for i in list:
		for k,v in i.items():
			print(k)
			print(v)
			for j,l in v.items():
				print(k,j,l)
for j in range(9):

	jj()
