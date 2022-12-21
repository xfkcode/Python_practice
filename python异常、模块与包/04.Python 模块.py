# [from 模块名] import [模块|类|变量|函数|*] [as 别名]
# 1.import 模块
# 模块.功能()
import time # python内置模块（time.py) ctrl+鼠标点击 可以打开源码
print("开始")
time.sleep(5)
print("结束")
# 2.from 模块 import 功能（类、变量、函数）
# 功能()
from time import sleep    # 函数
print("开始")
sleep(5)
print("结束")
# 3.from 模块 import * （全部功能导入）
# 功能()
from time import *
print("开始")
sleep(5)
print("结束")
# 4.as 别名
import time as t
t.sleep(5)
from time import sleep as sl
sl(5)