# -*- coding:utf-8 -*-
import requests

try:
    url = "http://www.baidu.com"
    r = requests.get(url)
    #以下是打印信息
    print (r.content.decode())
    print (r.headers)
    print (r.reason)
    print (r.cookies)
    for cookie in r.cookies:
        print (cookie.name,":",cookie.value)
    print (r.request)
except Exception as e:
    print (e)

