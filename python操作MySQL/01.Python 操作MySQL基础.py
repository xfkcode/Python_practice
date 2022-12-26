from  pymysql import Connection

conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='112358Xfk',
    autocommit=True             # 自动提交
)
print(conn.get_server_info())

cursor = conn.cursor()      #获取游标对象
# 选择数据库
conn.select_db('test')
# 执行非查询sql（创建表）
# cursor.execute('create table test_pymysql(id int);')
# 执行查询sql
cursor.execute('select * from test_pymysql')

results = cursor.fetchall()
for r in results:
    print(r)

# 插入数据
cursor.execute('insert into test_pymysql values(6),(7);')
# conn.commit()

conn.close()



