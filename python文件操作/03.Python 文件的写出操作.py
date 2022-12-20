# 打开文件
f = open("./write.txt","w",encoding="UTF-8")
# 文件写入
f.write("Hello World!!!")     # 内容写到内存中
# flush刷新
f.flush()                     # 将内存中积攒的内容，写到硬盘中
# 关闭文件
f.close()                     # 内置flush
# "w"文件不存在创建，存在清空写入
with open("./write.txt","w",encoding="UTF-8") as f:
    for i in range(5):
        f.write("xfk love tq\n")
        f.flush()