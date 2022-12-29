import re

s = 'itheima Python 12*&^@## 54638 xfk 哈哈'

# 找出所有数字
ret1 = re.findall(r"\d",s)           # 字符串前加r表示该字符串转义字符无效
print(ret1)
# 找出特殊字符
ret2 = re.findall(r"\W",s)           # 字符串前加r表示该字符串转义字符无效
print(ret2)
# 找出英文字母
ret3 = re.findall(r"[a-zA-Z]",s)
print(ret3)
# 匹配账号，只能由字母和数字组成，长度限制6-10
s = '736193'
r = '^[0-9a-zA-Z]{6,10}$'
print(re.findall(r,s))
# 匹配QQ号，要求纯数字，长度5-11，第一位不为0
r = '^[1-9][0-9]{4,10}$'
s = '491915216'
print(re.findall(r,s))
# 匹配邮箱地址，只允许qq、163、gmail这三种邮箱地址
r = '(^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$)'
s = 'a.s.d.e.s.d@qq.com'
print(re.findall(r,s))      # findall方法会返回正则表达式内所有分组结果

print(re.match(r,s))