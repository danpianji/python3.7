# -*- coding: UTF-8 -*-
"""
1--使用Requests库，访问鬼吹灯网页
2--使用BeautifulSoup解析网页
3--获得列表，使用json保存
"""
import requests
from bs4 import BeautifulSoup
import json

url = "http://seputu.com/"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'}
response = requests.get(url,headers=headers)
#print(response.text)
content=[]
soup = BeautifulSoup(response.text, 'lxml')#内置html.parser lxml的xml\lxml html5lib的html5lib共3种解析器
for mulu in soup.find_all(class_="mulu"):
    h2 = mulu.find('h2')
    if(h2!=None):
        h2_title = h2.string
        list=[]
        for a in mulu.find(class_='box').find_all('a'):
            href = a.get('href')
            box_title = a.get('title')
            list.append({'href':href, 'box_title':box_title})
        content.append({'title':h2_title, 'content':list})
with open("guihuideng.json", 'w') as f:
    json.dump(content, fp=f, indent=4)


