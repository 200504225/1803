def phone(dh):
	if dh.startswith("1") and len(dh) == 11:
		return True
	else:
		return False


dh = input("请输入手机号")
jj = phone(dh)
if jj == False:
	print("手机号错误")
	
dh = input("请输入手机号")
jj = phone(dh)
if jj == False:
	print("手机号不对")
