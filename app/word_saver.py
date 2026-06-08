# 项目一
word_dict={}
print("你好")
while True:
    word=input("请输入单词(输入exit退出)：")
    if word=="exit":
        break
    meaning=input("请输入含义：")
    word_dict[word]=meaning

with open("test.txt","w",encoding="utf-8")as f:
        for w,m in word_dict.items():
            f.write(f"{w}:{m}\n")
print("已经保存到 test.txt")
    
with open("test.txt","r",encoding="utf-8")as f:
        content=f.read()
print(content)

# 项目二 读取文件内容
with open("test.txt","r",encoding="utf-8")as f:
    #   列表
      lines=f.readlines()
for line in lines:
      word,meaning=line.strip().split(":")
      print(f"{word}->{meaning}")