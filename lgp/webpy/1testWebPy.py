# -*- coding: UTF-8 -*-
import web

urls = (

    '/index', 'index',
    '/demo/\d+','demo',
    '/(.*)', 'hello',

)

class index:
    def GET(self):
        data=web.input()
        return data
class demo:
    def POST(self):
        data = web.input()#获取请求参数
        return data
    def GET(self):
        return web.ctx.env#获得请求头信息

class hello:
    def GET(self,name):
        # with open('__init__.py', 'r') as f:
        #     content = f.read().encode('utf-8')
        #     return content+name
        return 'hello'+name

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

    #web.py
    # Chances are they 'll need to change:
    #
    # yield next(seq)
    #
    # to:
    #
    # try:
    #     yield next(seq)
    # except StopIteration:
    #     return
