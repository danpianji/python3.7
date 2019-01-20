# -*- coding: UTF-8 -*-
import requests
from lxml import etree
import urllib.request

#处理图片下载进度函数
def Schedule(blocknum, blocksize, totalsize):
    '''
    :param blocknum: 已下载数据块
    :param blocksize: 数据块大小
    :param totalsize: 远程文件大小
    :return:
    '''
    per = 100.0*blocknum*blocksize/totalsize
    if per>100:
        per = 100
    print ("当前下载进度：%d"%per)

url = "http://www.ivsky.com/tupian/ziranfengguang/"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'}
response = requests.get(url,headers=headers)

html = etree.HTML(response.text)
image_urls = html.xpath('.//img/@src')
print(len(image_urls))
i=0
for url in image_urls:
    urllib.request.urlretrieve(url, 'image_'+str(i)+'.jpg', Schedule)
    i+=1