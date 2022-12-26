"""
SQL 案例，读取文件，写入MySQL
"""
from file_define import TextFileReader,JsonFileReader
from data_define import Record
from  pymysql import Connection

text_file_reader = TextFileReader("./data/2011年1月销售数据.txt")
json_file_reader = JsonFileReader("./data/2011年2月销售数据JSON.txt")

jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()
# 将两个月的数据合并
all_data: list[Record] = jan_data + feb_data

# 构建MySQL连接对象
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='112358Xfk',
    autocommit=True             # 自动提交
)
# 获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db('test')
# 组织SQL语句
for record in all_data:
    sql = f"insert into orders(order_date,order_id,money,province) " \
          f"values('{record.date}','{record.order_id}','{record.money}','{record.province}')"
    # 执行SQL语句
    cursor.execute(sql)
# 关闭MySQL连接对象
conn.close()