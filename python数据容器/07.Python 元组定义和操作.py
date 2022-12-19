# (1,2,3,4,5)
# tup = (1,2,3,4,5)
# tup = ()
# tup = tuple()
t1 = (1,"666","xfk")
t2 = ()
t3 = tuple()
print(f"t1的类型{type(t1)}，内容是：{t1}")
# 单元素元组类型是元素类型，加逗号可以变为元组
t4 = ("string")
t5 = ("string",)
print(f"t4的类型{type(t4)}，内容是：{t4}")
print(f"t5的类型{type(t5)}，内容是：{t5}")
# 嵌套
t6 = ((1,2,1,1,1,1),(1,2))
print(f"t6的类型{type(t6)}，内容是：{t6}")
# 下标索引
num = t6[0][0]
print(f"t6[0][0]元素：{num}")
# 查找
index = t6[0].index(1)
print(f"t6元组0，1元素引索：{index}")
# 统计
print(f"t6元组0，1元素个数：{t6[0].count(1)}")
# 长度
print(f"t6元组元素个数：{len(t6)}")
# while遍历
i = 0
while i<len(t6):
    print(f"t6元组第{i+1}元素{t6[i]}")
    i+=1
# for遍历
for j in t6:
    print(f"t6元组元素{j}")
# 不可修改，嵌套list可修改
t7 = (1,2,[1,2,3])
print(f"修改前{t7}")
t7[2][0]="xfk"
t7[2].append(1)
print(f"修改后{t7}")





