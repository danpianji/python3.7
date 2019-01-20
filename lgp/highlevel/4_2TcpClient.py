# -*- coding: UTF-8 -*-

import socket

clientSocket = socket.socket()
hostname = socket.gethostname() # 获取本地主机名
port = 12345 # 设置端口号

clientSocket.connect((hostname, port))
strRecv = clientSocket.recv(1024)
print strRecv
clientSocket.send("客户端已接收，即将结束链接")
clientSocket.close()