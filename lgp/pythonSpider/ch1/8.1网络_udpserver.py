# -*- coding: UTF-8 -*-

#1、创建套接字、绑定ip和port
#2、发送数据和接收数据
#3、关闭套接字
import socket

if __name__=="__main__":
    #1、创建socket，连接服务端
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("127.0.0.1", 9999))
    print ("udp server begin...........")
    while True:
        #接收和发送数据
        data, address = s.recvfrom(1024)
        print ("client info...%s" % data.decode("utf-8"))
        print ("client address...%s, %s" % address)
        s.sendto(b"hello client, i am server", address)