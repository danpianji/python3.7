# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
#请求
url = "http://zhizhu.com/login"
user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
referer = "http://zhizhu.com"
postdata = {"username":"qiye",
            "password":"qiye_pass"}
#info 需要被编码为urllib2能理解的格式，这里用到的是urllib
headers = {"User_Agent":user_agent, "Referer":referer}
data = urllib.parse.urlencode(postdata).encode("utf-8")
request = urllib.request.Request(url, data, headers)
#响应
response = urllib.request.urlopen(request)
htmldata = response.read().decode("utf-8")
print (htmldata)