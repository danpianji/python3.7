# -*- coding: UTF-8 -*-

from gevent import monkey; monkey.patch_all()
import gevent
import urllib.request
from gevent.pool import Pool

def run_task(url):
    print ("visit----------%s" % url)
    try:
        rep = urllib.request.urlopen(url)
        data = rep.read()
        print ("%d byte received from %s " % (len(data), url))
    except Exception:
        print (e)
    return "url:%s ------>finished" % url


if __name__=="__main__":
    pool = Pool(2)
    urls = ["https://github.com", "https://www.python.org/", "http://www.cnblogs.com/", "http://www.baidu.com"]
    #greenlets = [gevent.spawn(run_task, url) for url in urls]
    #gevent.joinall(greenlets)
    result = pool.map(run_task, urls)
    print (result)