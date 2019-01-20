# -*- coding:utf-8 -*-
import requests
import chardet

try:
    url = "http://www.baidu.com"
    r = requests.get(url, stream=True)
    #以下是打印信息
    print (r.raw.read(10))
except Exception as e:
    print (e)

