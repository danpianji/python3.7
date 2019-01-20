# -*- coding:utf-8 -*-
import urllib.request
import urllib.response
class RedirectHandler(urllib.request.HTTPRedirectHandler):
    def http_error_301(self, req, fp, code, msg, headers):
        pass
    def http_error_302(self, req, fp, code, msg, headers):
        result = urllib.request.HTTPRedirectHandler.http_error_302(self, req, fp, code, msg, headers)
        result.status = code
        result.newurl = result.geturl()
        return result

opener = urllib.request.build_opener(RedirectHandler)
url = "http://www.baidu.com"
response = opener.open(url)
data = response.read().decode()
print (data)
print (response.geturl())