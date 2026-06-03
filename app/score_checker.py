# 3.项目练习
name=input("请输入姓名：")
score=int(input("请输入成绩："))

print("\n=====成绩分析=====")
print("姓名：",name)
print("成绩：",score)

if score>=90:
    print("等级：A")
elif score>=80:
    print("等级：B")
elif score>=70:
    print("等级：C")
elif score>=60:
    print("等级：D")
else:
    print("不及格，需要好好学习了。")