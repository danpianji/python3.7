# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.http import Request
import json
#导入webdriver
from selenium import webdriver
import time

#要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys
import sys
sys.path.append("..")
print(sys.path)
from  items import MyspiderweatherItem

# url = "http://www.weather.com.cn/weather/101010100.shtml"
class MyweatherSpider(scrapy.Spider):
    name = 'myweather'
    allowed_domains = ['weather.com.cn']
    base_url = 'http://www.weather.com.cn/weather/'
    start_urls = ['http://www.weather.com.cn/weather/101010100.shtml']
    dicCityUrl = {}
    def parse(self, response):
        item = MyspiderweatherItem()
        #找到输入框和搜索按钮
        #inputText = response.xpath("//input[@id='txtZip']")[0]
        #btnSearch = response.xpath("//input[@id='btnZip']")[0]
        #获得地区和时间信息
        divTop = response.xpath("//div[@class='ctop clearfix']")[0]
        city = divTop.xpath("./div[@class='crumbs fl']")[0]
        strCity = city.xpath("normalize-space(string(.))").extract()[0]
        time = divTop.xpath("./div[@class='time fr']")[0]
        strTime = time.xpath("normalize-space(string(.))").extract()[0]
        print(strCity,strTime)
        with open('weather.txt', 'ab+') as f:
            content = "\n*****************\n"+strCity+strTime
            f.write(content.encode('utf-8'))

        #获得7天的天气信息
        ul = response.xpath("//div[@id='7d']/ul[@class='t clearfix']")[0]
        lis = ul.xpath("./li")
        for li in lis:
            item["day"] = li.xpath("./h1/text()").extract()[0]
            item["wea"] = li.xpath("./p[@class='wea']/text()").extract()[0]
            tem = li.xpath("./p[@class='tem']")
            item["tem"] = tem.xpath('normalize-space(string(.))').extract()[0] #normalize-space去空格换行等，string(.)提取所有文本
            #获得风向
            spans = li.xpath("./p[@class='win']/em/span")
            windTitle = ""
            for span in spans:
                windTitle+=span.xpath("@title").extract()[0]+"_"
            #获得风力
            strwindLevel = li.xpath("./p[@class='win']/i/text()").extract()[0]
            item["wind"] = windTitle+strwindLevel
            #print (item)
            with open('weather.txt', 'ab+') as f:
                content = json.dumps(dict(item), ensure_ascii=False) + "\n"
                f.write(content.encode('utf-8'))
            #yield item #将item发送给pipelines存储

        inputCity = input()
        self.readCitys()
        newCode = self.dicCityUrl[inputCity]
        if len(newCode)>0:
            newUrl = self.base_url+newCode+".shtml"
            yield Request(url=newUrl, callback=self.parse)

    def readCitys(self):
        if self.dicCityUrl :
            return
        f = open("citycode.txt", "r", encoding='utf-8')  # 返回一个文件对象
        line = f.readline()  # 调用文件的 readline()方法
        while line:
            line = f.readline()
            if line.strip()=='':
                continue
            #获得城市代码行字符串，分割后保存到字典
            citycode = line.split('=')
            code = citycode[0].strip()
            city = citycode[1].strip()
            self.dicCityUrl[city]=code
        f.close()


# def autoSearch(city):
#     driver = webdriver.PhantomJS()
#     driver.set_window_size(1366, 768)
#     global url
#     driver.get(url)
#     driver.find_element_by_id('txtZip').send_keys(u'上海')
#     driver.find_element_by_id('btnZip').click()
#     url = driver.current_url
#     print("22222222222222222:",url)
#     return driver.page_source

if __name__ == '__main__':
    dic = {}
    dic["北京"]= '10000'
    print(dic)
    process = CrawlerProcess()
    process.crawl(MyweatherSpider)
    process.start()