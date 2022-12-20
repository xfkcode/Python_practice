# lambda 参数1,参数2,...:函数体（不能写多行）
# 只能使用一次
def func(computer):
    ret = computer(1,2)
    print(f"computer参数类型{type(computer)}")
    print(ret)
func(lambda x,y:x+y)