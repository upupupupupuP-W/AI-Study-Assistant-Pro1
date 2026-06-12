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


def analyze_student():
    if len(students)==0:
        print("暂无学生数据")
        return 
    total_student=len(students)
    print("学生人数：",total_student)
    total_score=0
    for student in students:
        total_score+=student["score"]
    average=total_score/total_student
    print('平均分：',average)
    highest=max(student["score"] for student in students)
    print("最高分：",highest)
    lowest=min(student["score"] for student in students)
    print('最低分：',lowest)


   
print("1.添加学生")
print("2.查看学生")
print('3.统计分析')
print("4.退出")

while True:

    choice=int(input("请输入你的选择："))
    
    if choice==1:
        add_student()
    if choice==2:
        show_students()
    if choice==3:
        analyze_student()
        

    if choice==4:
        break
    

