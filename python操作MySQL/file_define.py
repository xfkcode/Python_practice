"""
文件相关的类定义
"""
import json

from data_define import Record
# 抽象类
class FileRedaer:
    # 读取数据，转换为Record对象，封装成list返回
    def read_data(self) -> list[Record]:
        pass

class TextFileReader(FileRedaer):
    def __init__(self,path):
        self.path = path

    # 复写
    def read_data(self) -> list[Record]:
        f = open(self.path,"r",encoding="UTF-8")
        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip()         # 消除换行符\n
            data_list = line.split(",")

            record = Record(data_list[0],
                            data_list[1],
                            int(data_list[2]),
                            data_list[3]
                        )
            record_list.append(record)

        f.close()
        return record_list

class JsonFileReader(FileRedaer):
    def __init__(self,path):
        self.path = path

    # 复写
    def read_data(self) -> list[Record]:
        f = open(self.path,"r",encoding="UTF-8")
        record_list: list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)

            record = Record(data_dict["date"],
                            data_dict["order_id"],
                            data_dict["money"],
                            data_dict["province"]
                            )
            record_list.append(record)

        f.close()
        return record_list

# 测试
if __name__ == "__main__":
    text_file_reader = TextFileReader("./data/2011年1月销售数据.txt")
    json_file_reader = JsonFileReader("./data/2011年2月销售数据JSON.txt")
    list1 = text_file_reader.read_data()
    list2 = json_file_reader.read_data()

    for i in list1:
        print(i)
    for i in list2:
        print(i)
