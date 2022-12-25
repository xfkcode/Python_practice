# 类型注解（数据类型）
# 变量的类型注解
# 变量名: 类型
import json
import random

# 1.基础数据类型
var_1:int = 10
var_2:float = 10.0
var_3:bool = True
var_4:str = '1000'
# 2.类对象类型
class student:
    pass
stu:student = student()
# 3.基础容器类型
l1: list = [1,2,3]
t1: tuple = (1,2,3)
s1: set = {1,2,3}
d1: dict = {'1':1,'2':2}
string: str = "python"
# 4.容器类型详细注解
l2: list[int] = [1,2,3]
t2: tuple[str,int,bool] = ("xfk",27,True)       # 将每一个元素标记出来
s2: set[int] = {1,2,3}
d2: dict[str,int] = {'xfk':27}                  # 需要2个类型[key_type,value_type]

# 注释方法
var1 = random.randint(1,10)             # type: int
var2 = json.loads("{'name':'xfk'}")     # type: dict[str,str]
def func():
    return 10
var3 = func()                           # type: int
