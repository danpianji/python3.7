# -*- coding: UTF-8 -*-

import time, random
import threading


def fun_thread(urls):
    print "current thread %s is running....." % threading.currentThread().name
    for url in urls:
        print "%s----->> %s" % (threading.current_thread().name, url)
        time.sleep(random.random())
    print "current thread %s is end....." % threading.currentThread().name


if __name__=="__main__":
    print "thread %s is running....." % threading.currentThread().name
    t1 = threading.Thread(target=fun_thread, name="t1", args=(["url_1", "url_2", "url_3"],))
    t2 = threading.Thread(target=fun_thread, name="t2", args=(["url_4", "url_5", "url_6"],))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print "thread %s is end......" % threading.currentThread().name