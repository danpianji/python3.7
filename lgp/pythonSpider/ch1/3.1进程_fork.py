# -*- coding: UTF-8 -*-

import os

print "当前进程id：", os.getpid()

pid = os.fork()#非linux系统下运行出错：AttributeError: 'module' object has no attribute 'fork'

if pid != 0:
    print "错误."
elif pid == 0:
    print "父进程id %d , 子进程id %d" % (os.getppid(), os.getpid())