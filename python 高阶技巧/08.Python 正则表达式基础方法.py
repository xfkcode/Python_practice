import re

# match方法是从头部匹配
s = 'python itheima python'
ret1 = re.match("python",s)
print(ret1)
print(ret1.span())
print(ret1.group())

# search方法找到第一个匹配
ret2 = re.search("it",s)
print(ret2)

# findall方法找到所有匹配
ret3 = re.findall("python",s)
print(ret3)