# -*- coding: UTF-8 -*-
import multiprocessing
import random, time, os

def proc_send(pipe, urls):
    for url in urls:
        print "process %s send:%s" % (os.getpid(), url)
        pipe.send(url)
        time.sleep(random.random())


def proc_recv(pipe):
    while True:
        print "process %s recv:%s" % (os.getpid(), pipe.recv())
        time.sleep(random.random())#此代码会导致管道数据不能全部接收的问题


if __name__=="__main__":
    #创建管道
    pipe = multiprocessing.Pipe()

    #从创建进程
    p1 = multiprocessing.Process(target=proc_send, args=(pipe[0], ["url_"+str(i) for i in range(10)]))
    p2 = multiprocessing.Process(target=proc_recv, args=(pipe[1],))

    #启动进程
    p1.start()
    p2.start()

    #等待进程关闭
    p1.join()
    p2.terminate()#强制关闭