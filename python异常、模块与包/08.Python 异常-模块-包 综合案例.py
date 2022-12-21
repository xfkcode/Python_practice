# 创建自定义包my_utils
# str_util.py
# file_util.py

import my_utils.str_util
from my_utils import file_util

print(my_utils.str_util.str_reverse("Python"))
print(my_utils.str_util.substr("Python",0,4))

file_util.append_to_file("./abc.txt","itheima")
file_util.print_flie_info("./abc.txt")