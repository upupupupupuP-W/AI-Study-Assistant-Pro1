
try:
    x=int(input("请输入一个数字："))
    print(10/x)
except ValueError:
    print("输入错误：必须输入数字")
except ZeroDivisionError:
    print("错误，不可以除以0")



try:
    x=int(input("请输入一个数字："))
except ValueError:
    print("输入错误")
else:
    print(f"你输入的数字是{x}")
finally:
    print("无论是否有异常，都会执行")