# -*- coding: utf-8 -*-
import urllib.request

#本例子：timeout和返回代码
try:
    # 请求
    request = urllib.request.Request("http://www.baidu2.com")
    # 响应
    response = urllib.request.urlopen(request, timeout=2)
    data = response.read().decode()
    print (data)
    print (response.code,response.url)
except urllib.request.HTTPError as e:
    if hasattr(e, "code"):
        print ("error code:",e.code)
