# -*- coding:utf-8 -*-
import requests
#使用allow_redirects关键字=True允许重定向，可以使用history查看重定向后页面
r = requests.get("http://github.com", allow_redirects=True)
print (r.url)
print (r.status_code)
print (r.history)
#本例子：将http请求重定向为https请求
