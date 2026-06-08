
# print("Hello AI Study Assistant Pro")
# DAY2
# 1.认识变量
# name="张三"
# age=20
# score=95
# print("学生姓名:",name)
# print("学生年龄:",age)
# print("学生成绩",score)





# # 2.用户输入
# name=input("请输入姓名：")
# print("你好",name)
# school=input("请输入你的学校：")
# print("你的学校是：",school)




# # 3.数据类型
# name="wxt"
# age=20
# height=1.66
# is_student=True

# print(type(name))
# print(type(age))
# print(type(height))
# print(type(is_student))
# age1=input("请输入你的年龄:")
# print(type(age1))
# age2=int(age1)
# print(type(age2))




# # 4.条件判断
# score=int(input("请输入你的成绩："))
# if score>=60:
#     print("及格啦")
# else:
#     print("不及格")





# # 5.第一个模块，只能成绩分析器V1.0
# name=input("请输入学生姓名：")

# score=int(input("请输入学生成绩："))
# if score>=90:
#     print("等级：A")
# elif score>=80:
#     print("等级：B")
# elif score>=70:
#     print("等级：C")
# elif score>=60:
#     print("等级:D")   
# else:
#     print("等级:E")    









#  DAY3
# # # 1.if+else
# # age=int(input("请输入年龄："))
# # if age>=18:
# #     print("你已经成年了")
# # else:
# #     print("还未成年，要好好长大。")




# # 2.理解elif
# # score=int(input("请输入成绩："))
# # if score>=90:
# #     print("A")
# # elif score>=80:
# #     print("B")
# # elif score>=70:
# #     print("C")
# # elif score>=60:
# #     print("D")
# # else:
# #     print("你不及格啦，要好好努力学习哦。")





# # 3.项目练习
# name=input("请输入姓名：")
# score=int(input("请输入成绩："))

# print("\n=====成绩分析=====")
# print("姓名：",name)
# print("成绩：",score)

# if score>=90:
#     print("等级：A")
# elif score>=80:
#     print("等级：B")
# elif score>=70:
#     print("等级：C")
# elif score>=60:
#     print("等级：D")
# else:
#     print("不及格，需要好好学习了。")

# Day4
# for+range
# for i in range(5):
#     print(i)
# for i in range(2,5):
#     print(i)
# for i in range(0,10,2):
#     print(i)



# while循环
# n=5
# while n<=8:
#     print(n)
#     n+=1

  


# # DAY5
# # 1.学习函数
# def say_hello():
#     print("你好")

# say_hello()
# say_hello()

# DAY6
# 列表
# names=["Tom","Jack","Lucy"]

# DAY7
# # 字典 可以给数据取名字
# student={"name":"Tom","score":95}


# DAY8
# f=open("test.txt","w") 写模式，如果文件不存在会创建
# f.write("Hllo,Python!\n")
# f.close()
# r 读， w 写（覆盖），a,写（追加）,r+ 读写

# # 读写文件
# f=open("test.txt","r")
# content=f.read()
# # 读取整个文件
# print(content)
# f.close()

# # 按行读取
# f=open("test.txt","r")
# for line in f:
#     # print(line.strip())去掉换行符
# f.close()

# 写入文件
f=open("test.txt","w")
f.write("第一行\n")
f.write("第二行\n")
f.close()

# 追加内容
f=open("test.txt","a")
f.write("第三行\n")
f.close()

# 使用with自动关闭文件
with open ("test.txt","r") as f:
    content=f.read()
    print(content)
 
with open("test.txt","w") as f:
    f.write("第四行\n")

