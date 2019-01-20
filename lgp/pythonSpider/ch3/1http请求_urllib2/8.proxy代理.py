# -*- coding:utf-8 -*-
import urllib.request

proxy = urllib.request.ProxyHandler({"http":"127.0.0.1:8087"})
opener = urllib.request.build_opener(proxy)#代理设置错误会导致打开网页失败
url = "http://www.zhizhu.com"
response = opener.open(url)
data = response.read()
#print data
print (response.geturl())