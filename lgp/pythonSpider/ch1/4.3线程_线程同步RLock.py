# -*- coding: UTF-8 -*-

import random
import threading
import time

lock = threading.RLock()
num = 0
class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def run(self):
        global num
        while True:
            lock.acquire()
            print "thread %s locked, num=%d......" % (threading.currentThread().name, num)
            if num>=4 :
                lock.release()
                print "thread %s released, num=%d......" % (threading.currentThread().name, num)
                break
            num += 1
            print "thread %s released, num=%d......" % (threading.currentThread().name, num)
            lock.release()


if __name__=="__main__":
    print "thread %s is running....." % threading.currentThread().name
    t1 = myThread(name="t1")
    t2 = myThread(name="t2")

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print "thread %s is end......" % threading.currentThread().name