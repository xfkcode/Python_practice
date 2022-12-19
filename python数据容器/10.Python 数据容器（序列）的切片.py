# 起始下标：结束下标（不含）：步长
# list切片
l1 = [0,1,2,3,4,5,6]
sublist1 = l1[1:4]
print(f"切片结果：{sublist1}")
sublist2 = l1[3:1:-1]
print(f"切片结果：{sublist2}")
# tulpe切片
t1 = (0,1,2,3,4,5,6)
subtulpe1 = t1[:]
print(f"切片结果：{subtulpe1}")
subtulpe2 = t1[::-2]
print(f"切片结果：{subtulpe2}")
# str切片
string1 = "0123456"
substr1 = string1[::2]
print(f"切片结果：{substr1}")
substr2 = string1[::-1]
print(f"切片结果：{substr2}")

