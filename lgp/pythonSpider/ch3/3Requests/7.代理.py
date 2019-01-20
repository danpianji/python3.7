# -*- coding:utf-8 -*-
import requests
#使用allow_redirects关键字=True允许重定向，可以使用history查看重定向后页面
proxies = {
    "http":"http://202.98.197.245:3128",#从https://www.kuaidaili.com/free/intr/2/找的一个免费代理
   # "http":"http://user:password@host/"#host     10.10.1.11:2222
}
r = requests.get("http://github.com", proxies=proxies)#链接不上代理，会打印错误
print (r.url)
print (r.status_code)
print (r.history)
#本例子：将http请求重定向为https请求
