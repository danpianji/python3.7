# -*- coding: utf-8 -*-
import urllib.request
#请求
request = urllib.request.Request("http://zhizhu.com")
#响应
response = urllib.request.urlopen(request)
data = response.read()
print (data)