# 字符串只读，不可以修改
string="xfk tq"
# 下标索引访问
value1 = string[2]
value2 = string[-1]
print(value1,value2)
# index方法
print(f"字符串xfk引索值为：{string.index('xfk')}")
# replace方法
new_string=string.replace("tq","baby")
print(f"原字符串{string}，替换字符串{new_string}")
# split方法
split_string_list = string.split(" ")
print(f"切分字符串{split_string_list}，类型{type(split_string_list)}")
# strip方法（头尾）
# 默认去除首尾空格和换行符，有指定头尾子字符串（单字符）就去除
string2=" itheima python "
print(f"原字符串{string2}，strip()后：{string2.strip()}")
string3="ititheima pythonti"
print(f"原字符串{string3}，strip('it')后：{string3.strip('it')}")
# 统计
print(f"字符串it个数：{string3.count('it')}")
# 长度
print(f"字符串长度：{len(string3)}")
# while遍历
i = 0
while i<len(string3):
    print(f"字符串string3元素：{string3[i]}")
    i+=1
# for遍历
for j in string3:
    print(f"字符串string3元素：{j}")
