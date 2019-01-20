# -*- coding: UTF-8 -*-

import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

s.bind((host, port))

s.listen(5)
print "服务端已启动，等待客户端链接......"
while 1:
    sock, addr = s.accept()
    print "客户端地址:",addr
    sock.send("服务端已连接")
    str = sock.recv(1024)
    print str
    sock.close()
    break
