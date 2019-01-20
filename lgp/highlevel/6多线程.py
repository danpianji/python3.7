# -*- coding: UTF-8 -*-
import thread
import time
print "你好"
"""
Python中使用线程有两种方式：函数或者用类来包装线程对象。

1、函数方式
函数式：调用thread模块中的start_new_thread()函数来产生新线程。
语法如下:
thread.start_new_thread ( function, args[, kwargs] )
参数说明:
    function - 线程函数。
    args - 传递给线程函数的参数,他必须是个tuple类型。
    kwargs - 可选参数。

2、线程的结束
线程的结束一般依靠线程函数的自然结束；
也可以在线程函数中调用thread.exit()，他抛出SystemExit exception，达到退出线程的目的。 

"""


# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print "%s: %s %s" % (threadName, time.ctime(time.time()), time.asctime(time.localtime()))


# 创建两个线程
try:
    thread.start_new_thread(print_time, ("Thread-1", 2,))
    thread.start_new_thread(print_time, ("Thread-2", 4,))
except:
    print "Error: unable to start thread"

while 1:
    pass