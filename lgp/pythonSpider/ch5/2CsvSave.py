# -*- coding: UTF-8 -*-

import requests
from lxml import etree
import json
import re
import csv
url = "http://seputu.com/"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'}
response = requests.get(url,headers=headers)
html = etree.HTML(response.text)

pattern = re.compile("\s*\[(.*)\]\s+(.*)")
rows=[]
mulu = html.xpath('//div[@class="mulu"]')
for div_mulu in mulu:
    div_h2 = div_mulu.xpath(".//h2/text()")
    if len(div_h2)>0:
        title_h2 = div_h2[0]
        a_s = div_mulu.xpath("./div[@class='box']/ul/li/a")
        for a in a_s:
            href = a.get("href")
            title = a.get("title")

            match = re.match(pattern, title)
            if match!=None:
                date = match.group(1)
                real_title = match.group(2)
                content = (title_h2, real_title, href, date)
                print (content)
                rows.append(content)
headers = ['title', 'real_title', 'href', 'date']
with open("guichuideng.csv", 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)