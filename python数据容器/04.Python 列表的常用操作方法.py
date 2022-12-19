mylist = [12,34,56]
# 元素查询下标（不存在报错）
index = mylist.index(12)
print(f"12在list中的索引值为：{index}")
# 修改特定引索元素值（赋值）
mylist[1] = 89
print(f"修改后{mylist}")
# 插入指定引索位置新元素
mylist.insert(1,11)
print(f"插入后{mylist}")
# 追加新元素
mylist.append(666)
print(f"追加后{mylist}")
# 追加一批元素（容器）
mylist.extend([1,2,3])
print(f"追加list后{mylist}")
# 删除指定引索元素
del mylist[2]
print(f"删除后{mylist}")
# pop元素（指定引索元素并返回）
ret= mylist.pop(2)
print(f"删除元素{ret}")
print(f"删除后{mylist}")
# remove元素（第一个匹配元素移除）
mylist.remove(666)
print(f"删除后{mylist}")
# 清空
mylist.clear()
print(f"清空后{mylist}")
# 统计指定元素个数
mylist = [1,1,1,1,2,2,3]
print(f"元素1的个数：{mylist.count(1)}")
# 统计list全部元素数量
print(f"mylist元素个数：{len(mylist)}")









