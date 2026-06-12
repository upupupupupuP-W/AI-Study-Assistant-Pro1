def  get_grade(score):
    if score>=90:
        return "A"
    elif score>=80:
        return "B"
    elif score>=70:
        return "C"
    elif score>=60:
        return "D"
    else:
        return "F"
students=[]
def add_student():
    name=input("请输入学生姓名：")
    score=int(input("请输入学生成绩："))
    student={"name":name,"score":score,"grade":get_grade(score)}
    students.append(student)
    print(student)
    print("添加成功")

def show_students():
    print("\n==========学生列表===========")
    for student in students:
        print(student["name"],student["score"],student["grade"])

add_student()
add_student()
add_student()
show_students()
   
    