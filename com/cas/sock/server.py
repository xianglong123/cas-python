import socket
import sys

# 创建socket对象
socketSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

port = 9999

# 绑定端口号
socketSocket.bind((host, port))

# 设置最大连接数，超过后排队
socketSocket.listen(5)

while True:
    # 建立客户端连接
    clientSocket, addr = socketSocket.accept()
    print("连接地址: %s" % str(addr))
    msg = '欢迎连接' + "\r\n"
    clientSocket.send(msg.encode('utf-8'))
    clientSocket.close()
