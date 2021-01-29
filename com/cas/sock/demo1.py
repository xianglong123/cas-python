import socket

# 创建套接字
skt = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# 设置地址可重用
skt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 绑定主机和端口
skt.bind(('0.0.0.0', 8889))

# 监听服务
skt.listen(5)

if __name__ == '__main__':
    while True:
        print('waiting for connection...')
        tcpCliSock, addr = skt.accept()
        print('...connnecting from:', addr)

        while True:
            data = tcpCliSock.recv(1024)
            if not data:
                break
            print(data)
        tcpCliSock.close()
