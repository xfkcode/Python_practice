l = [['a',33],['b',55],['c',11]]

# 排序，基于带名排序
def choose_sort_key(ele):
    return ele[1]
l.sort(key=choose_sort_key,reverse=True)
print(l)
# 排序，基于lambda匿名函数
l.sort(key=lambda ele:ele[1],reverse=False)
print(l)