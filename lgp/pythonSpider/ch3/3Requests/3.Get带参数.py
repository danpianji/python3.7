# -*- coding:utf-8 -*-
import requests
import chardet

try:
    url = "http://www.baidu.com"
    params = {"sw":"python"}
    user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
    headers = {"User_Agent": user_agent}
    r = requests.get(url, params=params, headers=headers)
    #以下是打印信息
    print ("status_code:",r.status_code)
    print ("headers:",r.headers)
    print ("agent:",r.headers.get("Content-Encoding"))
    print (r.url)
    print (r.content)
    print (r.text)
    print (r.encoding)
    print ("content 编码:",chardet.detect(r.content))
    r.encoding = "utf-8"
    print(r.text)
except Exception as e:
    print (e)

