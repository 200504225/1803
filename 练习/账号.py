acc = "123456"
pwd = "abc"
s_acc = input("请输入账号")
s_pwd = input("请输入密码")
if (s_acc == acc and s_pwd == pwd):
	print("登陆成功")
elif(s_acc != acc and s_pwd == pwd):
	print("账户错误")
elif( s_acc == acc and s_pwd != pwd):
	print("密码错误")
else:
	print("傻子")
