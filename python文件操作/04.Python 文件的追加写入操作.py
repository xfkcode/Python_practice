with open("./write.txt","a",encoding="UTF-8") as f:
    for i in range(2):
        f.write("it Python Pycharm\n")   # 内容写到内存中
        f.flush()                        # 将内存中积攒的内容，写到硬盘中
# "a"文件不存在创建文件，存在追加内容