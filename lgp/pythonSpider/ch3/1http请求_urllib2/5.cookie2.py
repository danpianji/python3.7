# -*- coding:utf-8 -*-
import urllib.request

#通过设置请求头中的cookie处理
opener = urllib.request.build_opener()
opener.addheaders.append(("Cookie","email=xxx@163.com"))
url = "http://www.zhizhu.com/"
req = urllib.request.Request(url)
response = opener.open(req)
print (response.headers)
print (response.read().decode("utf-8"))