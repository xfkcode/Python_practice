def func(computer):
    ret = computer(1,2)
    print(f"computer参数类型{type(computer)}")
    print(ret)
def computer(x,y):
    return x+y
func(computer)
# 计算逻辑的传递，而非数据的传递