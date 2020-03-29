# 元组
# 数组/列表[]  list
# 字典


#判断        python是用缩进(四个空格)来代表代码块
a = 1
b = 2

if a ==1
    print("hahaha")

if a > b:                # 代码块(四个空格)
    print("a比b大")
else:
    print("b更大")

age = int(input("请输入你的年龄:"))    #从上到下运行，不存在同时满足多个条件
if age > 60:
    print("退休")
elif age > 30:
    print9("成家立业")
elif age > 20:
    print("好好学习")
else:
    print("天天向上")


if age > 20 and age <=30
    print("2222")
elif age > 30:
    print("3333")
elif age > 60:
    print("6666")
else:
    print("xxxxx")

# == 判断是否相等
# = 赋值



a = "你好"
if a in "你好，今天你吃了吗":  # in后可以是字符串，也可以是字典
    print("ok")
else:
    print("不ok")


a =  input("请输入:")
if a == "":
    print("不能为空！")
    exit()
if a in "0123455667":
    a = int(a)
else:
    print("请输入正确的年龄！")
    exit()     # 退出
if a > 5 :
    print("大")
else:
    print("小")

a = "safasfas"
if type(a) is int:
    print("是数字!")
elif type(a) is str:
    print("是字符串！")
else:
    print("其他")

# 循环

a = 1
while a < 10:
    print("哈哈哈",a)   # 死循环，Ctrl+C终止
    a = a + 1


# 遍历
a = "青城徐来，仙风自带"
for i in a:  # i 是遍历 a 中的每一个值
    print(i)

b = list(range(0,100,2)) #自动生成了一个数列,步进/步长
print(b)

for i in range(100):
    print(i)

#打印九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(i,"×",j,"=",i*j,end=" ") #end的作用不换行
    print()  #换行  