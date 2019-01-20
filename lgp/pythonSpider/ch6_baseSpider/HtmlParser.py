# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import re
import urllib.parse
class HtmlParser:
    def parser(self, page_url, page_cont):
        if page_url is None or page_cont is None:
            return
        soup = BeautifulSoup(page_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, page_cont)
        new_datas = self._get_new_data(page_url, page_cont)
        return new_urls,new_datas

    def _get_new_urls(self, page_url, soup):
        new_urls=set()
        links=soup.find_all('a', href=re.compile(r'/view/\d+\.htm'))
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        data={}
        data['url']=page_url

        title = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title']=title.get_text()

        summary = soup.find('div', class_='lemma-summary')
        data['summary']=summary.get_text()

        return data