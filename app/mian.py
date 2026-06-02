
print("Hello AI Study Assistant Pro")
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





# 5.第一个模块，只能成绩分析器V1.0
name=input("请输入学生姓名：")

score=int(input("请输入学生成绩："))
if score>=90:
    print("等级：A")
elif score>=80:
    print("等级：B")
elif score>=70:
    print("等级：C")
elif score>=60:
    print("等级:D")   
else:
    print("等级:E")    
