print("欢迎来到动物园")
# height = int(input("请输入您的身高（CM）："))
# vip_level = int(input("请输入你的VTP等级（1-5）:"))
# day = int(input("今天几号："))
if int(input("请输入您的身高（CM）：")) < 120:
    print("身高小于120CM，可以免费")
elif int(input("请输入你的VTP等级（1-5）:")) > 3:
    print("VIP级别大于3，可以免费")
elif int(input("今天几号：")) == 1:
    print("今天一号，免费")
else:
    print("需要买票10元")