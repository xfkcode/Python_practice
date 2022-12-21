"""
文件处理相关模块
"""
def print_flie_info(filename):
    """
    Function: 将给定路径文件输出打印
    :param filename: 文件路径
    :return: None
    """
    f = None
    try:
        f = open(filename,"r",encoding="UTF-8")
        content = f.read()
        print("文件全部内容如下：")
        print(content)
    except Exception as e:
        print(f"程序出现异常，原因是：{e}")
    finally:
        if f:
            f.close()

def append_to_file(filename,data):
    """
    Function: 文件追加内容
    :param filename: 文件路径
    :param data: 追加数据
    :return: None
    """
    f = open(filename,"a",encoding="UTF-8")
    f.write(data)
    f.write("\n")
    f.close()

# 测试代码
if __name__ == '__main__':
    print_flie_info("./test.txt")
    append_to_file("./test.txt","Python")