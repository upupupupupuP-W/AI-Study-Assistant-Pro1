def show_menu():
    print("\n========AI Study Assitant=========")
    print("1.添加学生")
    print("2.查看学生")
    print("3.退出")
students=[]

def add_student():
    name=input("请输入学生姓名：")
    score=int(input("请输入学生成绩："))
    student={"name":name,"score":score}
    students.append(student)
    print("添加成功")

def show_students():
    print("\n========学生列表=========")
    for student in students:
        print(student["name"])
        print(student["score"])

while True:
    show_menu()
    choice=input("请选择：")
    if choice=="1":
        add_student()
    elif choice=="2":
        show_students()
    elif choice=="3":
        print("程序结束")
        break
    else:
        print("输入错误")

   
      