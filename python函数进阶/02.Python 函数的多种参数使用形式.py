def func(name,age=18,gender="男"):
    print(f"姓名：{name}, 年龄：{age}，性别：{gender}")
# 位置，顺序匹配
func("xfk",27,"男")
# 关键字key=value（形参=实参），顺序不固定
func(name = "tq",age = 22,gender = "女")
# 缺省参数（必须在最后面）
func("xfk")
# 不定长 - 位置不定长，*号（元组）
def function1(*args):
    print(f"args类型{type(args)}，内容{args}")
function1(1,2,3,'xfk')
# 不定长 - 关键字不定长，**号（字典）
def function2(**kwargs):
    print(f"kwargs类型{type(kwargs)}，内容{kwargs}")
function2(name='xfk',age=11)