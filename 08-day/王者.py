acc = "123456"
pwd = "123456"
a = 1
while True:
	s_acc = input("请输入账号")
	s_pwd = input("请输入密码")
	if s_acc == acc and s_pwd == pwd:
		xz = int(input(" 0-ADC 1=肉盾 2-法师 "))
		if xz == 0:
			print("狄仁杰")
		elif xz == 1:
			print("刘邦")
		elif xz == 2:
			print("甄姬")
		break
	else:
		print("登录失败")
		a+=1
		if a == 4:
			print("账号冻结")
			break
