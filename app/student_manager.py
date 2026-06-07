# student={}
# student["name"]=input("请输入你的姓名：")
# student["score"]=int(input("请输入你的分数："))
# print("学生信息")
# for key,value in student.items():
#     print(key,":",value)


students=[]
while True:
    print("/n======学生管理系统======")
    print("1.添加学生")
    print("2.查找学生")
    print("3.退出")
    choice=int(input("请选择："))
    if choice==1:
        name=input("请输入名字：")
        score=input("请输入成绩：")
        student={"name":name,"score":score}
        students.append(student)
    elif choice==2:
        for student in students:
            print(student)
    elif choice==3:
        print("退出")
        break
    else:
        print("输入错误")