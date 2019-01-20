# -*- coding: UTF-8 -*-

#多进程模块导入进程
import os
from multiprocessing import Process

def run_proc(name):
    print "child process %s (%d) Running ......" % (name, os.getpid())

if __name__ == "__main__":
    print "parent process %s" % os.getpid()
    for i in range(5):
        p = Process(target=run_proc, args=(str(i),))
        print "process will start"
        p.start()
    p.join()
    print "process end"
