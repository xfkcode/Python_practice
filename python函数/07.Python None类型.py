print(type(None))
# >>> <class 'NoneType'>
# 用在函数无返回值
def func():
    print("hello world")
ans = func()
print(f"无返回值函数，返回内容是：{ans}")
print(f"无返回值函数，返回内容类型是：{type(ans)}")
# 用在if判断：None等同False
def check_age(age):
    if age>18:
        return "SUCCESS"
    else:
        return None
ret = check_age(16)
if not ret:
    print("未成年，不可进入")
# 用于声明无内容的变量
name = None
