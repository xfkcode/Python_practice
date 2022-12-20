# 打开文件
f = open("./test.txt","r",encoding="UTF-8")
print(f"f文件对象类型{type(f)}")
# >>>f文件对象类型<class '_io.TextIOWrapper'>文本类型文件操作
# 读取操作
# 1.read(num)读取num字节，没有参数就读取文件全部
print(f"读取32个字节：{f.read(32)}")
# 再次调用不会从头开始，从上次结束的位置开始
print(f"读取剩余全部内容：{f.read()}")
# 2.readlines()按行读取，返回list，其中每一个元素就是一行的数据
lines = f.readlines()
print(f"lines对象的类型：{type(lines)}")
print(f"lines对象的内容：{lines}")
# 3.readline()一次读取一行
lines = f.readline()
print(f"lines对象的类型：{type(lines)}")
print(f"第一行内容：{lines}")
lines = f.readline()
print(f"lines对象的类型：{type(lines)}")
print(f"第二行内容：{lines}")
# for循环读取
for line in f:
    print(f"{line}")
# 文件关闭
f.close()
# with open语法，自动关闭
with open("./test.txt","r",encoding="UTF-8") as f:
    for line in f:
        print(f"{line}")