# -*- coding: UTF-8 -*-
class UrlManager:
    def __init__(self):
        self.new_urls=set()
        self.old_urls=set()

    def has_new_url(self):
        #判断是否存在新的url
        return self.new_urls_size()!=0

    def get_new_url(self):
        #返回url
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def add_new_url(self, url):
        #添加url
        if url is None:
            return
        if url in self.new_urls or url in self.old_urls:
            return
        self.new_urls.add(url)

    def add_new_urls(self, urls):
        #添加url列表
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)

    def new_urls_size(self):
        #返回新url大小
        return len(self.new_urls)

    def old_urls_size(self):
        #返回旧url大小
        return len(self.old_urls)

