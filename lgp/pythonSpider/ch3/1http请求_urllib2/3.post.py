# -*- coding: utf-8 -*-

from urllib import parse
import urllib.request
#请求
url = "http://zhizhu.com/login"
postdata = {"username":"qiye",
            "password":"qiye_pass"}
#info 需要被编码为urllib2能理解的格式，这里用到的是urllib
data = parse.urlencode(postdata).encode("utf-8")
request = urllib.request.Request(url, data)
#响应
response = urllib.request.urlopen(request)
htmldata = response.read().decode("utf-8")
print (htmldata)