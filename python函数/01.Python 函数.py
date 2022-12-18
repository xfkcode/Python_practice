str1 = "itheima"
str2 = "python"
str3 = "pycharm"
def count_str(str):
    count = 0
    for i in str:
        count += 1
    return count
print(f"string1\"{str1}\"长度为：{count_str(str1)}")
print(f"string2\"{str2}\"长度为：{count_str(str2)}")
print(f"string3\"{str3}\"长度为：{count_str(str3)}")
