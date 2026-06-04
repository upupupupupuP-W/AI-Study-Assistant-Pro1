secret=7
answer=int(input("请输入你的答案："))
while secret!=answer:
    if answer>secret:
        print("你猜的数字大了，再来一次！")
    else:
        print("你猜的数字小了，再来一次！")
    answer=int(input("请输入你的答案："))
print("恭喜你答对了！")