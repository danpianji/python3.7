# -*- coding:utf-8 -*-
import requests
from requests.models import Response
try:
    url = "http://www.baidu.com"
    postdata = {"name":"xx","pwd":"123456"}
    r = requests.post(url, data=postdata)
    #以下是打印信息
    print (r.content)

except Exception as e:
    print (e)

"""
request的其他请求
r = requests.put(url, postdata)
r = requests.delete(url)
r = requests.head(url)
r = requests.options(url)
"""


