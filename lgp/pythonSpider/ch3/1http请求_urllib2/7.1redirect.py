# -*- coding:utf-8 -*-
import urllib.request
#检查是否重定向，response的url和request的url是否一致
url = "http://www.baidu.com"
response = urllib.request.urlopen(url, timeout=2)
url2 = response.geturl()
#code = response.getcode()
#info = response.info()
#print url2,"\n",code,"\n",info
if url2==url:
    print ("未重定向")
else:
    print ("重定向网址:",url2)

