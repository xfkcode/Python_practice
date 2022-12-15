# print("hello")
# print("world")
# print("hello",end='')
# print("world")
# print("hello world")
# print("itheima best")
# print("hello\tworld")
# print("itheima\tbest")

i = 1
while i<=9:
    j = 1
    while j<=i:
        print(f"{j}*{i}={j*i}\t",end='')
        j += 1
    print()
    i += 1