d1 = {"xfk":88}
print(f"{d1}")
# 新增/更新 字典[key]=value
d1["tq"]=90
print(f"增加后{d1}")
d1["xfk"]=100
print(f"更新后{d1}")
# 删除pop(key)返回被删除的value
score = d1.pop("tq")
print(f"删除{score}后{d1}")
# 获取全部key
print(f"字典d1全部key：{d1.keys()}，类型是：{type(d1.keys())}")
# 遍历
for key in d1.keys():
    print(f"字典d1的key是：{key}")
    print(f"字典的value是：{d1[key]}")
for key in d1:
    print(f"字典d1的key是：{key}")
    print(f"字典的value是：{d1[key]}")
# 长度
print(f"字典d1长度{len(d1)}")