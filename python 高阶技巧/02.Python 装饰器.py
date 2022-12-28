"""
装饰器
"""
def sleep():
    import random
    import time
    print("睡眠中.....")
    time.sleep(random.randint(1,5))

sleep()
# 装饰器一般写法（闭包）
def outer(func):
    def inner():
        print("我睡觉了")
        func()
        print("我起床了")

    return inner

fn = outer(sleep)
fn()

# 装饰器的快捷写法（语法糖）
@outer
def sleep():
    import random
    import time
    print("睡眠中.....")
    time.sleep(random.randint(1,5))

sleep()