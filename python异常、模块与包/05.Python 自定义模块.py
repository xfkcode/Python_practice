# 自定义模块
import module1
print(module1.test(1,2))
# 注意：两个模块有同名功能，执行后者（后者覆盖前者）
from module1 import test
from module2 import test
print(test(1,2))
# __main__变量
# 模块导入代码会被执行，若要使得一些代码（模块测试代码）不被执行需要用该变量
# if __name__ == '__main__': test()
from module1 import test
from module2 import test
# __all__变量作用*
from module1 import *
test(1,2)
# TEST(1,2) 不能使用，因为__all__变量没有包含TEST()