string = "万过薪月，员序程马黑来，nohtyp学"
# 先倒序再切片
str_result1 = string[::-1][9:14]
print(f"结果：{str_result1}")
# 先切片在倒序
str_result2 = string[5:10][::-1]
print(f"结果：{str_result2}")
# split分割“，” replace替换 倒序
str_result3 = string.split("，")[1].replace("来","")[::-1]
print(f"结果：{str_result3}")


