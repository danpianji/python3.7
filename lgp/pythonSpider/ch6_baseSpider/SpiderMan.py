# -*- coding: UTF-8 -*-

import DataOutput
import UrlManager
import HtmlDownloader
import HtmlParser

class SpiderMan:
    def __init__(self):
        self.manager=UrlManager.UrlManager()
        self.downloader=HtmlDownloader.HtmlDownloader()
        self.parser=HtmlParser.HtmlParser()
        self.output=DataOutput.DataOutput()

    def crawl(self, root_url):
        self.manager.add_new_url(root_url)
        while(self.manager.has_new_url() and self.manager.old_urls_size()<100):
            try:
                url = self.manager.get_new_url()
                html = self.downloader.download(url)
                new_urls, new_datas = self.parser.parser(url, html)
                self.manager.add_new_urls(new_urls)
                self.output.store_data(new_datas)
            except Exception as e:
                print ("crawl failed")
        self.output.output_html()

if __name__=="__main__":
    spider_man=SpiderMan()
    spider_man.crawl("https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB")


