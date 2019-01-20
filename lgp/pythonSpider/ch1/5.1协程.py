# -*- coding: UTF-8 -*-
import gevent
from gevent import  monkey
import  urllib.request
def run_task(url):
    print ("visit----------%s" % url)
    try:
        rep = urllib.request.urlopen(url)
        data = rep.read()
        print ("%d byte received from %s " % (len(data), url))
    except e:
        print (e)


if __name__=="__main__":
    monkey.patch_all()
    urls = ["https://github.com", "https://www.python.org/", "http://www.cnblogs.com/", "http://www.baidu.com"]
    greenlets = [gevent.spawn(run_task, url) for url in urls]
    gevent.joinall(greenlets)