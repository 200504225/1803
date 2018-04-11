acc = "123457"
pwd = "123456"
money = 100000#这是整数

s_acc = input("请输入账号")
s_pwd = input("请输入密码")

if s_acc == acc and s_pwd == pwd:
	s_money = float(input("请输入取款金额"))#浮点数

	if s_money <= money:
		print("已取%.02f元,剩余%.02f元"%(s_money,money-s_money))
	else:
		print("没钱取毛线")
else:
	print("无效账户")
