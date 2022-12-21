# python包
# 若干 .py模块 + __init__.py

# 1.模块级别导入方式1
# import 包.模块
# 包.模块.功能()
import package.module1
import package.module2
print(package.module1.TEST(1,2))
print(package.module2.test(1,2))
# 2.模块级别导入方式2
# form 包 import 模块
# 模块.功能()
from package import module1
from package import module2
print(module1.test(2,3))
print(module2.test(2,3))
# 3。功能级别导入
# form 包.模块 import 功能
# 功能()
from package.module1 import TEST
from package.module2 import test
print(TEST(3,4))
print(test(3,4))

# __all__变量作用*，写在__init__.py文件中
# 控制模块的导入
from package import *
print(module1.test(4,5))
# module2(4,5) __all__变量不包含module2,无法导入


