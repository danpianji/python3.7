# -*- coding: UTF-8 -*-

import socket
import threading
import time


def dealClient(sock, addr):
    #4、接收传来的数据，并发送数据给对方
    print ("收到客户端连接....%s,%s" % addr)
    sock.send(b"hello I'am server")
    while True:
        data = sock.recv(1024)
        if not data or data.decode("utf-8")=="exit":
            break
        print ("accept client data:%s" % data.decode("utf-8"))
        sock.send(("loopMsg:%s" % data.decode("utf-8")).encode("utf-8"))
    #5、关闭socketsock.close()

    print ("客户端连接关闭%s,%s" % addr)


if __name__=="__main__":
    #1、创建socket，绑定ip和端口
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 9999))
    #2、开始监听
    s.listen(5)
    print ("等待客户端连接.............")
    while True:
        #3、接收连接
        sock, addr = s.accept()
        #创建线程、处理连接
        t = threading.Thread(target=dealClient, args=(sock,addr))
        t.start()