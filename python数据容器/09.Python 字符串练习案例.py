string = "itheima Python Pycharm"
num = string.count("it")
print(f"字符串{string}中有‘it’{num}个")
new_string = string.replace(" ","|")
print(f"字符串{string}替换空格后{new_string}")
string_strip = new_string.strip("|")
print(f"字符串{new_string}分割后{string_strip}")