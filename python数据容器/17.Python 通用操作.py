l = [1,2,3,4,5]
t = (1,2,3,4,5)
string = "12345"
s = {1,2,3,4,5}
d = {"key1":1,"key2":2,"key3":3,"key4":4,"key5":5}
# len()
print(f"列表\t\t元素个数{len(l)}")
print(f"元组\t\t元素个数{len(t)}")
print(f"字符串\t元素个数{len(string)}")
print(f"集合\t\t元素个数{len(s)}")
print(f"字典\t\t元素个数{len(d)}")
# max()
print(f"列表\t\t最大元素{max(l)}")
print(f"元组\t\t最大元素{max(t)}")
print(f"字符串\t最大元素{max(string)}")
print(f"集合\t\t最大元素{max(s)}")
print(f"字典\t\t最大元素{max(d)}")
# min()
print(f"列表\t\t最小元素{min(l)}")
print(f"元组\t\t最小元素{min(t)}")
print(f"字符串\t最小元素{min(string)}")
print(f"集合\t\t最小元素{min(s)}")
print(f"字典\t\t最小元素{min(d)}")
# 类型转换
# 1。转list
print(f"列表转列表{list(l)}")
print(f"元组转列表{list(t)}")
print(f"字符串转列表{list(string)}")
print(f"集合转列表{list(s)}")
print(f"字典转列表{list(d)}")
# 2.转tuple
print(f"列表转元组{tuple(l)}")
print(f"元组转元组{tuple(t)}")
print(f"字符串转元组{tuple(string)}")
print(f"集合转元组{tuple(s)}")
print(f"字典转元组{tuple(d)}")
# 3.转str
print(f"列表转字符串{str(l)}")
print(f"元组转字符串{str(t)}")
print(f"字符串转字符串{str(string)}")
print(f"集合转字符串{str(s)}")
print(f"字典转字符串{str(d)}")
# 4.转set
print(f"列表转集合{set(l)}")
print(f"元组转集合{set(t)}")
print(f"字符串转集合{set(string)}")
print(f"集合转集合{set(s)}")
print(f"字典转集合{set(d)}")
# 排序sorted结果list，默认从小到大
print(f"列表排序{sorted(l,reverse=True)}")
print(f"元组排序{sorted(t,reverse=True)}")
print(f"字符串排序{sorted(string,reverse=True)}")
print(f"集合排序{sorted(s,reverse=True)}")
print(f"字典排序{sorted(d,reverse=True)}")