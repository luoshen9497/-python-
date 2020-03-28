# a = (1,2,3,4,5,"luoluo","np","qingcheng")
# b = (a,6,7,8)
# print(b[0][2])
# a = [1,2,3,4,"xixi","haha",True,False]
# print(a[4])
# a.append("kawayi")
# print(a)
# print(a.clear())
# xx = ["ailigei",888]
# a.extend(xx)
# print(a)
# print(a+xx)
# a.remove(1)  #删除某个值，*括号里面的内容不是下标
# b = a.remove(1)
# print(b)
# print(a)
# 注意：True=1 ，False=0
# xx = [0,False,1,True] 
# a = xx.count(0)
# print(a)



# a = [1,2,3,4,"xixi","haha",True,False]
# a.remove(1)
# print(a)
#取值get
# a = {"name":"洛洛",0:"xixi","age":99}
# # print(a["name"])
# # #新增 pop
# # a["high"] = "183cm"
# # print(a)
# # #修改/update
# # a["name"] = "青城"
# # print(a)
# # b = a.get("name")
# # print(b)
# b = a.pop("name":"luoluo")
# print(b)


a = {"name":"洛洛",0:"xixi","age":99}
# print(a)
#剪切
# a.pop("name")
# print(a)

# print(a.get("name22")) # a.get("name22")是空，所以print为None
# print(a["name22"])# 代码会报错
#数组和字典的删除
# del a ["name"]
# print(a)

# del a[0]
# del a ["name"]
# print(a)
del a[2]
print(a)