nums = [1,2,3,4,5,6]
def list_while_func(nums):
    i = 0
    while i < len(nums):
        print(nums[i])
        i += 1
def list_for_func(nums):
    for j in nums:
        print(j)
list_for_func(nums)
list_while_func(nums)
