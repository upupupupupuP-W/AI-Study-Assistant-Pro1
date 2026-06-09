# while True:
#     try:
#         age=int(input("请输入你的年龄："))
#         if age<0:
#             raise ValueError("年龄不为负数")
#         break
#     except ValueError as e:
#         print(f"输入错误：{e}")
    
# print(f"年龄是：{age}")


try:
    with open("test.txt","r",encoding="utf-8") as f:
        content=f.read()
except FileNotFoundError:
    print("文件不存在，请先创建文件")
except Exception as e:
    print(f"读取文件时出现错误：{e}")
