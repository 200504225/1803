s_acc = "123456"
s_pwd = "abc"

acc = int(input("请输入账号"))
pwd = str(input("请输入密码"))
if acc == s_acc and pwd == s_pwd:
	print("登录成功")
elif acc == s_acc:
	print("密码不正确")
elif pwd == s_pwd:
	print("账户不正确")
else:
	print("账号为空")
