def func1():
    print("func1开始执行")
    num = 1/0
    print("func1结束执行")
def func2():
    print("func2开始执行")
    func1()
    print("func2结束执行")
def main():
    try:
        func2()
    except Exception as e:
        print(f"出现异常，异常信息：{e}")
main()