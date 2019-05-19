# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import item,Field

class MyspiderweatherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    day = Field() # 日期
    wea = Field() # 天气
    tem = Field() # 温度
    wind = Field() # 风力

    pass
