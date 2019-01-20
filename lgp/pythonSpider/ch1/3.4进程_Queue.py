# -*- coding: UTF-8 -*-
from multiprocessing import Process, Queue
import os, time, random


def fun_write(q, urls):#向队列写数据
    print "进程%s 向队列写数据" % os.getpid()
    for url in urls:
        q.put(url)
        print "put %s to queue" % url
        time.sleep(random.random())


def fun_read(q):#从队列读取数据
    print "进程%s 从队列读取数据" % os.getpid()
    while True:
        url = q.get(True)
        print "get %s from queue" % url


if __name__ == "__main__":#主函数
    q = Queue()

    #创建进程
    proc_write1 = Process(target=fun_write, args=(q, ['url_1','url_2','url_3']))
    proc_write2 = Process(target=fun_write, args=(q, ['url_4','url_5','url_6']))

    proc_read = Process(target=fun_read, args=(q,))

    #启动进程
    proc_write1.start()
    proc_write2.start()

    proc_read.start()

    #等待进程结束
    proc_write1.join()
    proc_write2.join()
    #由于read进程是死循环，所有只能强制结束
    proc_read.terminate()

