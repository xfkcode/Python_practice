nums = [21,235,56,78,34,22,22]
nums.append(31)
nums.extend([19,33,30])
num1 = nums[0]
print(f"nums第一个元素：{num1}")
num2 = nums[-1]
print(f"nums最后一个元素：{num2}")
index =  nums.index(22)
print(f"元素22引索：{index}")
print(nums)