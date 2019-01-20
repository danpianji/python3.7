# -*- coding: UTF-8 -*-
import os, time, random
from multiprocessing import Pool

def run_task(name):
    print "process name=%s (pid=%d)" % (name, os.getpid())
    time.sleep(random.random()*3)
    print "process %s end" % name

if __name__ == "__main__":
    print "main process %s" % os.getpid()
    p = Pool(processes=3)
    for x in range(5):
        p.apply_async(run_task, args=(str(x),))#Pool执行函数，apply执行函数,当有一个进程执行完毕后，会添加一个新的进程到pool中
    print "waiting for all chid process done"
    p.close()
    p.join()#调用join之前，一定要先调用close() 函数，否则会出错, close()执行后不会有新的进程加入到pool,join函数等待素有子进程结束
    print "all process done"