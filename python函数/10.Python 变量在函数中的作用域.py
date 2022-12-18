def test1():
    # 局部变量
    num1 = 100
    print(num1)
    return
test1()
# print(num1)报错，num1为局部变量，只能在函数中使用
num2 = 1000
def test2():
    print(num2)
    return
def test3():
    num2 = 500
    print(num2)
    return
test2()
test3()
print(num2)
def test4():
    # 将函数内部变量声明为全局变量
    global num2
    num2 = 500
    print(num2)
    return
test4()
print(num2)