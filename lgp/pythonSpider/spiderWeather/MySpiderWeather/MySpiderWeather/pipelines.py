# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

class MyspiderweatherPipeline(object):

    def __init__(self):
        self.file = open('teacher.json', 'wb')
        print("hhhhhhhhhhhhhh")

    def process_item(self, item, spider):
        print("wwwwwwwwwwwww")
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(content)
        return item

    def open_spider(self, spider):
        # spider (Spider 对象) – 被开启的spider
        # 可选实现，当spider被开启时，这个方法被调用。
        pass

    def close_spider(self, spider):
        self.file.close()

