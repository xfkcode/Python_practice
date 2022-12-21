# 捕获异常
# try:
#     可能发生错误的代码
# except:
#     如果出现异常执行的代码
try:
    f = open("./abc.txt","r",encoding="UTF-8")
except:
    print("出现异常，因为文件不存在，将open'r'模式调整为'w'模式")
    f = open("./abc.txt", "w", encoding="UTF-8")
# 捕获指定异常
try:
    print(name)
    # 1/0
except NameError as e:
    print('name变量名称未定义错误')
    print(e)
# 捕获多个异常
try:
    # print(name)
    1/0
except (NameError,ZeroDivisionError) as e:
    print('变量未定义错误 或 除以0错误')
    print(e)
# 为正确设置捕获异常类型，将无法捕获
# 捕获所有异常
try:
    print(name)
    1/0
except Exception as e:
    print("出现异常")
    print(e)
# 捕获异常存在顺序，返回优先捕获到的异常
# else:无异常执行（可选）
try:
    pass
except Exception as e:
    print("出现异常")
    print(e)
else:
    print("没有发生异常")
# finally:无论是否发生异常都执行（可选）
try:
    f = open("./abc.txt","r",encoding="UTF-8")
except Exception as e:
    f = open("./abc.txt","w",encoding="UTF-8")
    print(e)
else:
    print("没有发生异常")
finally:
    f.close()