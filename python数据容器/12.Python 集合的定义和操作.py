# {1,2,3,4,5}
# s = {1,2,3,4,5}
# s = set()
# 不重复，无序
s1 = {"xfk","tq","lover","xfk","tq","lover"}
s_empty = set()
print(f"s1集合内容是：{s1}，类型是：{type(s1)}")
print(f"s_empty集合内容是：{s_empty}，类型是：{type(s_empty)}")
# 修改操作
# 1.添加add
s1.add("xiaosan")
s1.add("xfk")
print(f"添加后{s1}")
# 2.移除remove
s1.remove("xfk")
print(f"移除后{s1}")
# 3.随机取出一个元素
ret = s1.pop()
print(f"随机取出：{ret}，取出后{s1}")
# 4.清空
s1.clear()
print(f"清空后{s1}")
# 5.差集difference（s1去除s1和s2交集部分）
s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1.difference(s2)
print(f"s1和s2差集{s3}")
# 6.差集difference_update（修改s1）
s1 = {1,2,3}
s2 = {2,3,4}
s1.difference_update(s2)
print(f"s1消除s1和s2交集{s1}")
# 7.合并
s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1.union(s2)
print(f"s1和s2合并{s3}")
# 8.长度
s1 = {1,1,1,2,3,4,5}
print(f"集合s1长度{len(s1)}")
# 9。集合的遍历（only for）
s1 = {1,2,3,4,5}
for ele in s1:
    print(f"集合s1元素{ele}")

