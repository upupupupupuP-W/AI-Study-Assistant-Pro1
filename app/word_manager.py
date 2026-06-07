# 单词管理器V1
words=[]
while True:
    print("\n======单词管理器=======")
    print("1.添加单词")
    print("2.查看单词")
    print("3.退出")

    choice=int(input("选择："))
    if choice==1:
        word=input("输入单词：")
        words.append(word)
        print("添加成功")
    
    elif choice==2:
        print("\n当前单词：")
        for each in words:
            print(each)
    elif choice==3:
        print('退出程序') 
        break   
    else:
        print("输入错误")