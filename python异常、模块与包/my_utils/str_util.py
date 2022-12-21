"""
字符串处理相关模块
"""
def str_reverse(s):
    """
    Function: 字符串反转
    :param s: 字符串
    :return:  反转字符串
    """
    return s[::-1]
def substr(s,x,y):
    """
    Function: 字符串切片
    :param s: 字符串
    :param x: 开始下标
    :param y: 结束下标
    :return:  切片字符串
    """
    return s[x:y]

# 测试代码
if __name__ == '__main__':
    print(str_reverse("Python"))
    print(substr("Python",1,3))
