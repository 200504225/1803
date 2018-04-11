na=["嫦娥","哪吒","东海龙王","玉帝"]
for i in na:
	print("邀请%s来聚餐"%i)
print("%s因病无法赴约"%na[0])
na[1] = "耶稣"
for i in na:
	print("%s和我一起用餐"%i)
print("因为有了一个更大的饭店")
na.insert(0,"上帝")
na.insert(3,"太上老君")
na.append("如来")
for j in na:
	print("%s和我一起用餐"%i)
print("因为饭店太小只能邀请两个嘉宾")
for i in na:
	print("%s你别来了不好意思饭店不够大"%(na[0:5]))
