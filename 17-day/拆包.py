def sum(a,b,*args,**kwargs):
	c=a+b
	print(a)
	print(b)
	print(args)
	print(kwargs)
	return c


t = (3,4,5,6,7,8,9)
d = {"age":22}
print(sum(1,2,*t,**d))

