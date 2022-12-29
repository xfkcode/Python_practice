import socket

# 创建Socket对象
socket_client = socket.socket()
# 绑定IP和端口
socket_client.connect(("localhost",8888))
while True:
    # 发送消息
    msg = input("请发送消息：")
    if msg == 'exit':
        break
    socket_client.send(msg.encode('UTF-8'))
    # 接收消息
    recv_data = socket_client.recv(1024)
    print(f"服务端回复消息是：{recv_data.decode('UTF-8')}")

# 关闭连接
socket_client.close()