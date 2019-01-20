# -*- coding:utf-8 -*-
import requests
url = "http://www.baidu.com/login"
s = requests.session()
#首先访问登陆页面，作为游客，服务器会先分配一个cookie
r = s.get(url, allow_redirects=True)
datas = {"name":"qiye", "passwd":"123456"}
#向登陆链接发送post请求，验证成功，游客权限会转为会员权限
r = s.post(url, data=datas, allow_redirects=True)
print (r.text)