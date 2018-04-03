s_acc = "123456"
s_pwd = "abc"
s_mo = "1000000"
acc = int(input("请输入账号"))
pwd = int(input("请输入密码"))
if acc == s_acc and s_pwd == pwd:
	mo = float(input("请输入金额"))
	if mo<=s_mo:
		print("取款金额:%,余额:%f"%(mo,s_mo-mo))
	else:
		print('傻子')
else:
	print("无效账户")
