i=0 # 提前定义
for i in range(5):
    print(i)
# for循环临时变量不应在循环外访问（不是硬性要求）
print(i)