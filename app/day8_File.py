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

