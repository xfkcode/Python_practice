num = 5
if int(input("第一次猜测：")) == num:
    print("恭喜第一次猜对了")
elif int(input("猜错了，再猜一次：")) == num:
    print("猜对了")
elif int(input("猜错了，再猜一次：")) == num:
    print("恭喜，最后一次，猜对了")
else:
    print("猜错了")