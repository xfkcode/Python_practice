def func1():
    print("----2----")
def func2():
    print("----1----")
    func1()
    print("----3----")
func2()