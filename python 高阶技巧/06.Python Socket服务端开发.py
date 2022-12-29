import socket

# 创建Socket对象
socket_server = socket.socket()
# 绑定IP和端口
socket_server.bind(("localhost",8888))
# 监听端口
socket_server.listen()                  # 整数参数表示链接的数量
# 等待客户端连接
# accept()方法是阻塞方法，等待客户端链接，没有链接就卡在这不向下执行
conn,address = socket_server.accept()   # 返回二元元组(链接对象，客户端地址信息)
print(f"客户端连接，信息{address}")

while True:# 接收客户端信息
    data = conn.recv(1024).decode("UTF-8")
    # recv参数是缓冲区大小，一般给1024
    # recv返回一个字节数组bytes对象，不是字符串，可以decode转变为字符串
    print(f"客户端发来的消息是：{data}")
    # 发送恢复消息
    msg = input("请输入恢复消息：")
    if msg == 'exit':
        break
    conn.send(msg.encode("UTF-8"))

# 关闭连接
conn.close()
socket_server.close()