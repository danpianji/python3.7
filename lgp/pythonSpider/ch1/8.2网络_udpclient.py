# -*- coding: UTF-8 -*-

#1、创建套接字
#2、发送数据和接收数据
#3、关闭套接字
import socket


if __name__=="__main__":
    #1、创建socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = ("127.0.0.1", 9999)
    for str in [b"hello", b"world"]:
        s.sendto(str, addr)
        data, address = s.recvfrom(1024)
        print ("%s--%d" % (address[0], address[1]))
        print ("server info...%s" % data.decode("utf-8"))
    s.close()
