# -*- coding: UTF-8 -*-

import socket

if __name__=="__main__":
    #1、创建socket，连接服务端
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 9999))

    #2、发送和接收数据
    data = s.recv(1024)
    print ("accept server data:%s" % data.decode("utf-8"))
    s.send(b"hello I'am client")
    data = s.recv(1024)
    print ("accept server data:%s" % data.decode("utf-8"))
    s.send(b"exit")
    #3、关闭socket
    s.close()