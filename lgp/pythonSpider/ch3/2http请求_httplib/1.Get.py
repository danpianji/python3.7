# -*- coding:utf-8 -*-
import http.client
conn = None
try:
    url = "www.baidu.com"
    conn = http.client.HTTPConnection(url,port=80)
    conn.request("GET", "/")
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