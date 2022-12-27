"""
闭包
"""
def outer(logo):

    def inner(msg):
        print(f"<{logo}>{msg}<{logo}>")

    return inner

fn1 = outer("Pyhton")       # 返回函数（inner）
fn1("xfk")
fn1("tq")

fn2 = outer("Pycharm")
fn2("xfk")

# 使用nonlocal关键字修改外部函数的值
def Outer(num1):

    def Inner(num2):
        nonlocal num1
        num1 += num2
        print(num1)

    return Inner

fn = Outer(10)
fn(10)

# ATM案例
def account_create(init_amount=0):

    def ATM(num,deposit=True):
        nonlocal init_amount
        if deposit:
            init_amount += num
            print(f"存款+{num}，账户余额：{init_amount}")
        else:
            init_amount -= num
            print(f"取款+{num}，账户余额：{init_amount}")

    return ATM

atm = account_create()
atm(100)
atm(200)
atm(100,False)
