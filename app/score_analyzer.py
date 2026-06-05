def check(score):
    if score>=90:
        return "A"
    elif score>=80:
        return "B"
    elif score>=70:
        return "C"
    elif score>=60:
        return "D"
    else:
        return "没有及格，请继续努力！"
    
score=int(input("请输入学生成绩："))
grade=check(score)
print("成绩：",grade)