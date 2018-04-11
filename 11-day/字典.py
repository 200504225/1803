a = {"姓名":"薛栋炎","年龄":25,"性别":"男","民族":"汉"}
print(a)
#这是增
a["地址"] = "河南"
a.setdefault("身高",175)
print(a)
#这是删a.setdefault
a.pop("身高")
a.popitem()
print(a)
#这是改
a["姓名"] = "哪吒"

print(a)
#这是查
print(a["姓名"])
print(a.get("地址"))
#合并
a2 = {"身高":155,"体重":100}
a.update(a2)
print(a)


print(a.keys())
print(a.values())
print(a.items())
