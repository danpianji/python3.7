# -*- coding:utf-8 -*-
import urllib.request
import http.cookiejar

#使用CookieJar进行cookie的管理
cookie = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
url = "http://www.baidu.com"
response = opener.open(url)
for item in cookie:
    print (item.name, ":", item.value)