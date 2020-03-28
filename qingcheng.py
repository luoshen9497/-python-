# a = (1,2,3,4,"xixi","xixi","xixi","xixi","xixi","haha",True,False)
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[5])
# print(a[6])
# print(a[7])


#切片(批量取值)[x:y]
# print(a[-1])
# print(a[-2])
# print(a[-4])
# print(a[-6])
# print(a[0:5])
# print(a[:6])
# print(a[9:])


# # print(a.index("xixi"))  index/count 只能操作一维元组，不能操作二维元组
# # print(a.index("xixi"))
# # print(a.count("xixi")) #count()计算某个值的数量
# #二维元组
# b = (a,"xixi","hahaha")
# print(b[0][2])


# a = [1,2,3,4,"xixi","haha",True,False]
# print(a[4])
# a.append("fangsi") #append往数组尾巴上中追加数据
# a.insert(1,"np")   #inser往数组指定的位置插入数据，不可超出范围，超出范围则添加至末尾
# print(a)
#元组的优点：不可修改
#元组()和数组[]的区别:元组写好后不可修改，而数组是可以修改的
# a.pop(4)  #剪切
# print(a)
# b = a.pop(4)
# print(b)
# c = a.pop(1) #2被剪切
# d = a.pop(2) #此是下标2为4
# print(c+d) #2+4为6
# a.clear() #清空
# xx = ["面对恐惧",666]
# # a.extend(xx)  #合并数组
# # print(a)
# print(a+xx)
# print(a)
# a.remove(1)  #删除某个值，*括号里面的内容不是下标
# b = a.remove(1)
# print(b)
# print(a)
#注意：True=1 ，False=0
xx = [0,False,1,True]
a = xx.count(0)
print(a)

#对于元组或者数组操作时，注意下标不要超出范围--越界
xx = [0,1,2,3]
print(xx[9])    #会报错
"""
所有的方法都是小括号结尾，比如：print（），input（），lenI（）。
元组,数组，字典的取值，都是用中括号[]，比如a[9]
元组，数组，字典的定义，分别是：(),[]，{}
"""