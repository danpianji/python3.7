# -*- coding: UTF-8 -*-
"""

python对XML的解析

常见的XML编程接口有DOM和SAX，这两种接口处理XML文件的方式不同，当然使用场合也不同。

python有三种方法解析XML，SAX，DOM，以及ElementTree:
1.SAX (simple API for XML )
python 标准库包含SAX解析器，SAX用事件驱动模型，通过在解析XML的过程中触发一个个的事件并调用用户定义的回调函数来处理XML文件。

2.DOM(Document Object Model)
将XML数据在内存中解析成一个树，通过对树的操作来操作XML。

3.ElementTree(元素树)
ElementTree就像一个轻量级的DOM，具有方便友好的API。代码可用性好，速度快，消耗内存少。

注：因DOM需要将XML数据映射到内存中的树，一是比较慢，二是比较耗内存，
而SAX流式读取XML文件，比较快，占用内存少，但需要用户实现回调函数（handler）。
"""

import xml.sax

class moviesHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    #元素开始事件处理
    def startElement(self, name, attrs):
        self.CurrentData = name
        if name=="movie":
            print ("------ movie start ------")
            title = attrs["title"]
            print ("title=",title)

    #元素结束事件处理
    def endElement(self, name):
        if name=="type":
            print("type:",self.type)
        elif name=="format":
            print ("format:",self.format)
        elif name == "year":
            print ("year:", self.year)
        elif name == "rating":
            print ("rating:", self.rating)
        elif name == "stars":
            print ("stars:", self.stars)
        elif name == "description":
            print ("description:", self.description)


    #内容事件处理
    def characters(self, content):
        if self.CurrentData=="type":
            self.type = content
        elif self.CurrentData=="format":
            self.format = content
        elif self.CurrentData=="year":
            self.year = content
        elif self.CurrentData=="rating":
            self.rating = content
        elif self.CurrentData=="stars":
            self.stars = content
        elif self.CurrentData=="description":
            self.description = content


if ( __name__ == "__main__"):
    parser = xml.sax.make_parser() #创建sax解析器
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 重写 ContextHandler
    Handler = moviesHandler()
    parser.setContentHandler(Handler)

    parser.parse("movies.xml")

