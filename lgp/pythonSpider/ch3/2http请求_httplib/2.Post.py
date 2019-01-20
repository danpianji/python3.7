# -*- coding:utf-8 -*-
import http.client
import urllib.parse
conn = None
try:
    #post需要的用户名、密码等参数信息及请求消息头
    params = urllib.parse.urlencode({"name":"qiye", "age":23})
    headers = {"Content-type":"application/x-www-form-urlencoded", "Accept":"text/plain"}

    url = "www.zhizhu.com"
    conn = http.client.HTTPConnection(url,port=80,timeout=3)
    conn.request("POST", "/login", params, headers)
    response = conn.getresponse()
    print ("-"*40)
    print ("fileno:",response.fileno(), "version:",response.version, "status:",response.status, "reason:",response.reason)
    print ("msg:",response.msg)
    for head in response.getheaders():
        print ("head:",head)
    print ("data:",response.read().decode())
    print ("-"*40)
except Exception as e:
    print (e)
finally:
    if conn:
        conn.close()